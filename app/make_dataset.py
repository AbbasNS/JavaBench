import argparse
import glob
import os
from typing import Any, Dict

from tqdm import tqdm

from util.io import read_code, write_jsonl

def export_problems(project_id: str, project: Dict[str, Any], args: Dict[str, str]):
    def get_code_context(context_root: str, related_source_list: list[str]):
        context = []
        visited = {}

        for source in related_source_list:
            files = glob.glob(os.path.join(context_root, source))
            if len(files) == 0:
                raise FileNotFoundError(f"Cannot find {source} in {context_root}")
            for file in files:
                if visited.get(file) == True:
                    continue
                visited[file] = True
                context.append(read_code(file))

        return "\n".join(context)

    task_data = []
    for task_name, task in tqdm(project["tasks"].items()):
        task_id = f"{project_id}/{task_name}"
        code = read_code(os.path.join(project["todo_root"], task["target"]))

        if args.mode == "stripped-context":
            code_context = get_code_context(
                context_root=project["context_root"],
                related_source_list=task["related_source_list"],
            )
        elif args.mode == "full-context":
            code_context = get_code_context(
                context_root=project["todo_root"],
                related_source_list=task["related_source_list"],
            )[:args.max_context_len]
        elif args.mode == "no-context":
            code_context = ""
        task_data.append(
            dict(
                task_id=task_id,
                target=task["target"],
                code=code,
                code_context=code_context,
            )
        )

    write_jsonl(os.path.join(args.out_dir, f"data-{project_id}.jsonl"), task_data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=str, required=True)
    parser.add_argument("--max-context-len", type=int, default=8192)
    parser.add_argument(
        "--mode", 
        type=str,
        choices=["stripped-context", "full-context", "no-context"],
        default="stripped-context",
    )
    args = parser.parse_args()

    from datasets.descriptor.pa19 import project as project19
    export_problems("PA19", project19, args)
    from datasets.descriptor.pa20 import project as project20
    export_problems("PA20", project20, args)
    from datasets.descriptor.pa21 import project as project21
    export_problems("PA21", project21, args)
    from datasets.descriptor.pa22 import project as project22
    export_problems("PA22", project22, args)