import random
import time
from DynamicArray import DynamicArray

def generate_dynamic_array(size):
    arr = DynamicArray(size)
    upper_bound = max(size * 2, 1000)
    for _ in range(size):
        arr.add(random.randint(0, upper_bound))
    return arr

def _is_sorted(data):
    iterator = iter(data)
    try:
        prev = next(iterator)
    except StopIteration:
        return True
    for item in iterator:
        if prev > item:
            return False
        prev = item
    return True


def time_sort(algorithm, data, validate=False):
    start = time.perf_counter()
    algorithm(data)
    end = time.perf_counter()
    if validate and not _is_sorted(data):
        raise ValueError(f"{algorithm.__name__} failed to sort the data correctly")
    return round((end - start) * 1000, 3)  # milliseconds
