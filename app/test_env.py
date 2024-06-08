from io import StringIO
import subprocess
import shutil
import os
import re
import pandas as pd

from typing import List
from app.schema.schemas import CompilerError


def to_code_path(root, code_path):
    return os.path.join(root, "src", "main", "java", code_path)


class TestEnv:
    def __init__(self, root: str, todo_src: str, src: str) -> None:
        self.root = root
        self.todo_src = todo_src
        self.src = src
        shutil.copytree(src, root)

    def destory(self):
        shutil.rmtree(self.root)

    def replace(self, target: str, content: str):
        code_path = to_code_path(self.root, target)
        todo_code_path = to_code_path(self.todo_src, target)
        if not os.path.exists(code_path):
            print(f"warning: replace non-existed file {code_path}")
        # with open(code_path, "w") as fp:
        #     fp.write(content)

        with open(todo_code_path, "r") as fp:
            todo_content = fp.read()
        todo_content_start = todo_content.find("public")
        content_start = content.find("public")

        if todo_content_start == -1 or content_start == -1:
            return {
                "has_todo": False,
                "can_replace": False
            }

        with open(code_path, "w") as fp:
            fp.write(todo_content[:todo_content_start] + content[content_start:])

        return {
            "has_todo": "// TODO" in content[content_start:],
            "can_replace": True
        }

    def recover(self, target: str):
        shutil.copy2(to_code_path(self.src, target), to_code_path(self.root, target))

    def compile(self) -> List[CompilerError]:
        process = subprocess.Popen(
            ["./gradlew", "compileJava", "--info", "-q", "--rerun-tasks"],
            cwd=self.root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            env={"LANG": "en_US.UTF-8"},
        )
        _, err = process.communicate()
        errors1 = CompilerError.parse_errors(err_string=err.decode("utf-8"))


        process = subprocess.Popen(
            ["./gradlew", "compileTestJava", "--info", "-q", "--rerun-tasks"],
            cwd=self.root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            env={"LANG": "en_US.UTF-8"},
        )
        _, err = process.communicate()
        errors2 = CompilerError.parse_errors(err_string=err.decode("utf-8"))
        return errors1 + errors2

    def run_test(self, target: str | None):
        args = ["./gradlew", "test"]
        if target:
            args += ["--tests", target]
        args += ["--rerun-tasks"]
        process = subprocess.Popen(
            args,
            cwd=self.root,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            env={"LANG": "en_US.UTF-8"},
        )
        out, _ = process.communicate()
        out = out.decode()
        match = re.search(
            r"Results: (\w+) \((\d+) tests, (\d+) successes, (\d+) failures, (\d+) skipped\)",
            out,
        )
        return (int(match.group(3)), int(match.group(2))), out
    
    def run_dep_metrics(self):
        source_dir = "src/main/java"
        process = subprocess.Popen(
            [
                "java", "-jar", "./lib/java-sellotape.jar", "dep-metric",
                "--generated-project", os.path.join(self.root, source_dir),
                "--solution-project", os.path.join(self.src, source_dir),
                "--todo-project", os.path.join(self.todo_src, source_dir),
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env={"JAVA_TOOL_OPTIONS": "-Duser.language=en", "JAVA_HOME": "/usr/lib/jvm/default-runtime" },
        )
        out, err = process.communicate()
        out = out.decode()
        print(err.decode())
        
        out = pd.read_csv(StringIO(out), header="infer", sep="\s+")
        return out.iloc[0]
