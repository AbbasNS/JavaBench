import itertools
import json
import pandas as pd
import numpy as np
import os

# Universal

PA = ["PA19", "PA20", "PA21", "PA22"]
models = [
    "gpt-3.5-turbo-1106",
    # "gpt-4-0125-preview",
    "Phind-CodeLlama-34B-v2",
    "WizardCoder-15B-V1.0",
    "deepseek-coder-6.7b-instruct",
    "deepseek-coder-33b-instruct",
]

def estimate_pass_at_k(n, c, k):
    if n - c < k:
        return 1.0
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

def process_label(label):
    parts = label.split('-')
    method = parts[0]
    context = parts[1] if len(parts) > 1 else "sel"
    return method, context

def sample_count(records, *, n = 5, key = "task_id"):
    count = {}
    result = []
    for sample in records:
        if count.get(sample[key]) is None:
            count[sample[key]] = 0
        count[sample[key]] += 1
        if count[sample[key]] > n:
            continue
        result.append(sample)
    return result

def group_flat_data(flat_data):
    df = pd.DataFrame(flat_data)
    df = df.groupby(['PA', 'Model', 'Context', 'Method']).apply(
        lambda x: pd.Series({'Value': x['V1'].sum() / x['V2'].sum()})
    ).reset_index()
    df = df.pivot_table(index=['Context', 'Method', 'Model'], 
                        columns='PA', 
                        values='Value')
    return df

def concat_df(dfs):
    df = pd.concat(dfs).reset_index()
    df["Total"] = df[['PA19', 'PA20', 'PA21', 'PA22']].sum(axis=1)
    df = df.sort_values(by="Total", ascending=False)
    df = df.drop(columns=["Total"])
    return df

def style_df(df):
    df = df.style
    df = df.set_properties(**{'text-align': 'left', 'font-family': "monospace"})
    df = df.set_table_styles([
        dict(selector='th', props=[('text-align', 'left')]),
    ]).hide(axis="index")
    df = df.background_gradient(cmap="coolwarm", low=0.5, high=0.5, axis=0, subset=['PA19', 'PA20', 'PA21', 'PA22'])
    return df

# Table
def get_lazy_data(PA, models, *, label = "holistic", n = 5, k = 1):
    flat_data = []
    method, context = process_label(label)
    for pa in PA:
        for model in models:
            path = f"../output/{label}/result-{pa}/{model}/single_class.json"
            if not os.path.exists(path):
                print(f"Not Found: {path}")
                continue

            raw_result = sample_count(json.load(open(path)), n=n)
            result = {}
            for record in raw_result:
                task_id = record["task_id"]
                if not result.get(task_id):
                    result[task_id] = [0, 0]
                if record["can_replace"] and not record["has_todo"]:
                    result[task_id][0] += 1
                result[task_id][1] += 1
            for task_id, values in result.items():
                # print(f"{pa} {label} {model} {task_id} {values[0]} {values[1]}")
                assert values[1] == n
                flat_data.append({'PA': pa, 'Model': model, 'Context': context, "Method": method, 'V1': estimate_pass_at_k(n, values[0], k), 'V2': 1})
    return group_flat_data(flat_data)

def get_compilation_data(PA, models, *, mode = "full", label = "holistic", n = 5, k = 1):
    flat_data = []
    method, context = process_label(label)
    for pa in PA:
        for model in models:
            path = f"../output/{label}/result-{pa}/{model}/result-{mode}.json"
            if not os.path.exists(path):
                print(f"Not Found: {path}")
                continue

            raw_results = sample_count(itertools.chain.from_iterable(list(json.load(open(path)).values())), n=n, key="test_id")
            result = {}
            for record in raw_results:
                test_id = record["test_id"]
                if not result.get(test_id):
                    result[test_id] = [0, 0]
                if record["can_replace"] and not record["has_todo"] and record["compilable"]:
                    result[test_id][0] += 1
                result[test_id][1] += 1
            for test_id, values in result.items():
                assert values[1] == n
                flat_data.append({'PA': pa, 'Model': model, 'Context': context, "Method": method, 'V1': estimate_pass_at_k(n, values[0], k), 'V2': 1})
    return group_flat_data(flat_data)

def get_single_compilation_data(PA, models, *, label = "holistic", n = 5, k = 1):
    flat_data = []
    method, context = process_label(label)
    for pa in PA:
        for model in models:
            path = f"../output/{label}/result-{pa}/{model}/single_class.json"
            if not os.path.exists(path):
                print(f"Not Found: {path}")
                continue

            raw_result = sample_count(json.load(open(path)), n=n)
            result = {}
            for record in raw_result:
                task_id = record["task_id"]
                if not result.get(task_id):
                    result[task_id] = [0, 0]
                if record["can_replace"] and not record["has_todo"] and record["compile_errors"] == 0:
                    result[task_id][0] += 1
                result[task_id][1] += 1
            for task_id, values in result.items():
                assert values[1] == n
                flat_data.append({'PA': pa, 'Model': model, 'Context': context, "Method": method, 'V1': estimate_pass_at_k(n, values[0], k), 'V2': 1})
    return group_flat_data(flat_data)

def get_pass_data(PA, models, *, mode = "full", label = "holistic", n = 5, k = 1):
    flat_data = []
    method, context = process_label(label)
    for pa in PA:
        for model in models:
            path = f"../output/{label}/result-{pa}/{model}/result-{mode}.json"
            if not os.path.exists(path):
                print(f"Not Found: {path}")
                continue


            raw_results = sample_count(itertools.chain.from_iterable(list(json.load(open(path)).values())), n=n, key="test_id")
            result = {}
            for record in raw_results:
                test_id = record["test_id"]
                if not result.get(test_id):
                    result[test_id] = [0, 0]
                if record["can_replace"] and not record["has_todo"] and record["compilable"]:
                    result[test_id][0] += int(record["n_pass"][0]) / int(record["n_pass"][1])
                result[test_id][1] += 1
            for test_id, values in result.items():
                assert values[1] == n
                flat_data.append({'PA': pa, 'Model': model, 'Context': context, "Method": method, 'V1': estimate_pass_at_k(n, values[0], k), 'V2': 1})
    return group_flat_data(flat_data)

def get_single_pass_data(PA, models, *, label = "holistic", n = 5, k = 1):
    flat_data = []
    method, context = process_label(label)
    for pa in PA:
        for model in models:
            path = f"../output/{label}/result-{pa}/{model}/single_class.json"
            if not os.path.exists(path):
                print(f"Not Found: {path}")
                continue

            raw_result = sample_count(json.load(open(path)), n=n)
            result = {}
            for record in raw_result:
                task_id = record["task_id"]
                if not result.get(task_id):
                    result[task_id] = [0, 0]
                if record["can_replace"] and not record["has_todo"] and record["compile_errors"] == 0:
                    result[task_id][0] += int(record["test_result"][0]) / int(record["test_result"][1])
                result[task_id][1] += 1
            for task_id, values in result.items():
                assert values[1] == n
                flat_data.append({'PA': pa, 'Model': model, 'Context': context, "Method": method, 'V1': estimate_pass_at_k(n, values[0], k), 'V2': 1})
    return group_flat_data(flat_data)

def get_project_compilation_data(PA, models, *, label = "holistic", n = 5, k = 1):
    flat_data = []
    method, context = process_label(label)
    for pa in PA:
        for model in models:
            path = f"../output/{label}/result-{pa}/{model}/project_wise.json"
            if not os.path.exists(path):
                print(f"Not Found: {path}")
                continue

            records = json.load(open(path))
            n_pass = 0
            n_total = 0
            for i in range(n):
                record = records[i]
                if record["can_replace"] and not record["has_todo"] and record["compile_error"] == 0:
                    n_pass += 1
                n_total += 1
            assert n_total == n
            flat_data.append({'PA': pa, 'Model': model, 'Context': context, "Method": method, 'V1': estimate_pass_at_k(n, n_pass, k), 'V2': 1})
    return group_flat_data(flat_data)

def get_project_pass_data(PA, models, *, label = "holistic", n = 5, k = 1):
    flat_data = []
    method, context = process_label(label)
    for pa in PA:
        for model in models:
            path = f"../output/{label}/result-{pa}/{model}/project_wise.json"
            if not os.path.exists(path):
                print(f"Not Found: {path}")
                continue

            records = json.load(open(path))
            n_pass = 0
            n_total = 0
            for i in range(n):
                record = records[i]
                if record["can_replace"] and not record["has_todo"] and record["compile_error"] == 0:
                    n_pass += int(record["n_pass"][0]) / int(record["n_pass"][1])
                n_total += 1
            assert n_total == n
            flat_data.append({'PA': pa, 'Model': model, 'Context': context, "Method": method, 'V1': estimate_pass_at_k(n, n_pass, k), 'V2': 1})
    return group_flat_data(flat_data)

def join_all(A, B, C, D, E, orders = ['Model', 'Context', 'Method']):
    order_map = {
        "Context": ["maximum", "minimum", "selective"],
        "Method": ["holistic", "independent", "incremental", "incremental_rev", "incremental_random"],
        "Model": ["WizardCoder-15B-V1.0", "deepseek-coder-6.7b-instruct", "deepseek-coder-33b-instruct", "Phind-CodeLlama-34B-v2", "gpt-3.5-turbo-1106"]
    }

    merge_keys = list(order_map.keys())
    BC = pd.merge(B, C, on=merge_keys, suffixes=('_B', '_C'))
    DE = pd.merge(D, E, on=merge_keys, suffixes=('_D', '_E'))
    merged_df = A.merge(BC, on=merge_keys, how='left').merge(DE, on=merge_keys, how='left')

    final_df = merged_df[merge_keys + 
                         ['PA19', 'PA20', 'PA21', 'PA22',
                          'PA19_B', 'PA20_B', 'PA21_B', 'PA22_B', 
                          'PA19_C', 'PA20_C', 'PA21_C', 'PA22_C', 
                          'PA19_D', 'PA20_D', 'PA21_D', 'PA22_D', 
                          'PA19_E', 'PA20_E', 'PA21_E', 'PA22_E']]

    columns = pd.MultiIndex.from_tuples([
        ('', '', 'Context'), ('', '', 'Method'), ('', '', 'Model'),
        ('', 'Completion', 'P1'), ('', 'Completion', 'P2'), ('', 'Completion', 'P3'), ('', 'Completion', 'P4'),
        ('Compilation', 'class-wise', 'P1'), ('Compilation', 'class-wise', 'P2'), ('Compilation', 'class-wise', 'P3'), ('Compilation', 'class-wise', 'P4'),
        ('Compilation', 'test-wise', 'P1'), ('Compilation', 'test-wise', 'P2'), ('Compilation', 'test-wise', 'P3'), ('Compilation', 'test-wise', 'P4'),
        ('Pass', 'class-wise', 'P1'), ('Pass', 'class-wise', 'P2'), ('Pass', 'class-wise', 'P3'), ('Pass', 'class-wise', 'P4'),
        ('Pass', 'test-wise', 'P1'), ('Pass', 'test-wise', 'P2'), ('Pass', 'test-wise', 'P3'), ('Pass', 'test-wise', 'P4')
    ])

    final_df.columns = columns

    for (order_key, order_values) in order_map.items():
        final_df[('', '', order_key)] = pd.Categorical(final_df[('', '', order_key)], categories=order_values, ordered=True)
    df = final_df.sort_values(by=[('', '', order) for order in orders])

    df = df.style
    df.set_properties(**{'text-align': 'left', 'font-family': "monospace"})
    df.set_table_styles([
        dict(selector='th', props=[('text-align', 'left')]),
    ]).hide(axis="index")

    def color_gradient(val):
        color1 = np.array([255, 255, 255])
        color2 = np.array([135, 188, 166])
        val = float(val)
        color = (1 - val) * color1 + val * color2
        return f'background-color: rgb({int(color[0])}, {int(color[1])}, {int(color[2])})'

    target_columns = [col for col in final_df.columns if col[-1] not in merge_keys]
    df = df.applymap(color_gradient, subset=pd.IndexSlice[:, target_columns])

    return df