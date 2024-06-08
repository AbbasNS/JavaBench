import json
import matplotlib.pyplot as plt
import numpy as np

def sorted_multiple_columns_bar(ax, model_result_map, *, title: str, y_label="", legend_ncols=3, draw_lines=False):
    models = list(iter(model_result_map.keys()))
    keys = list(model_result_map[models[0]].keys())
    x = np.arange(len(keys))
    y_list = np.array([[round(model_result_map[model][key], 2) for key in keys] for model in models])
    y_sorted_indices = np.argsort(y_list, axis=0)[::-1]
    y_ranks = np.empty_like(y_sorted_indices)
    for col in range(y_list.shape[1]):
        y_ranks[y_sorted_indices[:, col], col] = np.arange(y_list.shape[0])

    width = 0.16
    legends = []
    for index, model_id in enumerate(models):
        offset = y_ranks[index] * width
        rects = ax.bar(x + offset, y_list[index], width, label=model_id)
        legends.append(rects)

        ax.bar_label(rects, padding=3)
        if draw_lines:
            ax.plot(x + offset, y_list[index], label=model_id, linestyle="dashed", marker='o', markeredgecolor='black', markersize=5, markeredgewidth=1)

    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xticks(x + width, [key.split('/')[-1] for key in keys])
    ax.legend(handles=legends, loc='upper left', ncols=legend_ncols)
    ax.set_ymargin(0.5)
    ax.relim()
    ax.autoscale_view()

def hist_plot(model_result_map, ncols = 8):
    models = list(iter(model_result_map.keys()))
    keys = list(model_result_map[models[0]].keys())
    nrows = (len(keys)- 1) // ncols + 1
    fig, ax = plt.subplots(nrows, ncols, layout='constrained', figsize=(35, 5 * nrows))
    ax = ax.flatten()
    for i, test_id in enumerate(keys):
        width = 0.16
        # 转换 + 填充数据
        y_list = [np.round(np.array(model_result_map[model][test_id]["test_distribution"]) / 50, 2) for model in models]
        max_length = max([len(y) for y in y_list])
        y_list = np.array([np.pad(row, (0, max_length - len(row))) for row in y_list])
        # 去零
        x_label = np.arange(max_length)[np.any(y_list != 0, axis=0)]
        y_list = y_list[:, np.any(y_list != 0, axis=0)]
        # 排序
        y_sorted_indices = np.argsort(y_list, axis=0)[::-1]
        y_ranks = np.empty_like(y_sorted_indices)
        x = np.arange(x_label.shape[0])
        for col in range(y_list.shape[1]):
            y_ranks[y_sorted_indices[:, col], col] = np.arange(y_list.shape[0])
        for index, model_id in enumerate(models):
            offset = y_ranks[index] * width
            rects = ax[i].bar(x + offset, y_list[index], width, label=model_id)
            ax[i].bar_label(rects, fmt=lambda x: x if x > 0 else '', padding=3)
        ax[i].set_xticks(x + width, x_label)
        ax[i].set_title(f"{test_id}")
        ax[i].relim()
        ax[i].autoscale_view()
    for i in range(len(keys), nrows * ncols):
        fig.delaxes(ax[i])


def line_plot(ax, model_result_map, *, title: str, y_label="", legend_ncols=3):
    for model_id, model_result in model_result_map.items():
        sorted_keys = sorted(model_result.keys())
        sorted_values = [model_result[key] for key in sorted_keys]
        ax.plot(sorted_keys, sorted_values, label=model_id)
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.legend(loc='upper left', ncols=legend_ncols)
    ax.set_ymargin(0.5)
    ax.relim()
    ax.autoscale_view()


def aggregate(data: str, *, k = "1,3,5", filter_todo = True):
    ks = k.split(",")
    aggregate_results = {}
    test_results = json.load(open(data, "r"))

    def estimate_pass_at_k(n, c, k):
        if n - c < k:
            return 1.0
        return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

    max_k = min(len(l) for l in test_results.values())
    for test_id, result in test_results.items():
        aggregate_results[test_id] = {}
        n_compilable = 0
        n_total = 0
        test_distribution = {}

        for i in range(max_k):
            if result[i]["compilable"] and result[i]["can_replace"] and (not filter_todo or not result[i]["has_todo"]):
                n_compilable += 1
                n_total = max(n_total, result[i]["n_pass"][1])
                n_pass = int(result[i]["n_pass"][0])
                if test_distribution.get(n_pass) is None:
                    test_distribution[n_pass] = 0
                test_distribution[n_pass] += 1
        aggregate_results[test_id]["test_distribution"] = [0] * (n_total + 1)
        for i in range(n_total + 1):
            aggregate_results[test_id]["test_distribution"][i] = test_distribution.get(i, 0)
        for k in ks:
            k = int(k)
            aggregate_results[test_id][f"pass_{k}"] = estimate_pass_at_k(
                max_k, n_compilable, k
            )
    return aggregate_results