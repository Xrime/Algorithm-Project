def quick_sort(arr):
    def partition(a, low, high):
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def _quick_sort(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            _quick_sort(a, low, pi - 1)
            _quick_sort(a, pi + 1, high)

    if len(arr) > 1:
        _quick_sort(arr, 0, len(arr) - 1)
    return arr
