import os
import platform

import matplotlib.pyplot as plt
import psutil
from bubble_sort import bubble_sort
from combine import generate_dynamic_array, time_sort
from counting_sort import counting_sort
from heap_sort import heap_sort
from insertion_sort import insertion_sort
from merge_sort import merge_sort
from quick_sort import quick_sort
from selection_sort import selection_sort

sizes = [500000, 800000, 1000000]
algorithms = {
    "Bubble": bubble_sort,
    "Insertion": insertion_sort,
    "Selection": selection_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Counting": counting_sort,
    "Heap": heap_sort,
}



def gather_system_info():
    info = {
        "Operating System": platform.platform(),
        "Processor": platform.processor() or "Unknown",
        "Logical Cores": os.cpu_count(),
    }
    if psutil:
        cpu_freq = psutil.cpu_freq()
        if cpu_freq:
            info["Processor Speed (MHz)"] = round(cpu_freq.max or cpu_freq.current, 2)
        total_ram = psutil.virtual_memory().total / (1024 ** 3)
        info["RAM (GB)"] = round(total_ram, 2)
    else:
        info["RAM (GB)"] = "Install psutil to capture"
    return info


def print_system_info(info):
    print("System properties:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()


def main():
    results = {name: [] for name in algorithms}
    print_system_info(gather_system_info())

    for size in sizes:
        print(f"\nSorting {size} elements...")
        base_data = generate_dynamic_array(size)
        for name, func in algorithms.items():
            dataset = base_data.copy()
            elapsed = time_sort(func, dataset, validate=True)
            results[name].append(elapsed)
            print(f"{name} Sort: {elapsed} ms")

    print("\nResults (milliseconds; '-' indicates skipped):")
    header = ["Size"] + list(algorithms.keys())
    print("".join(f"{col:>15}" for col in header))
    for idx, size in enumerate(sizes):
        row = [f"{size:15}"]
        for name in algorithms:
            value = results[name][idx]
            row.append(f"{value:15.3f}" if value is not None else f"{'-':>15}")
        print("".join(row))

    if plt:
        for name, times in results.items():
            filtered = [(s, t) for s, t in zip(sizes, times) if t is not None]
            if not filtered:
                continue
            plot_sizes, plot_times = zip(*filtered)
            plt.plot(plot_sizes, plot_times, marker='o', label=name)
        plt.xlabel("Input Size (n)")
        plt.ylabel("Time (ms)")
        plt.title("Sorting Algorithm Performance")
        plt.legend()
        plt.grid(True, linestyle='--', linewidth=0.5)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    main()

