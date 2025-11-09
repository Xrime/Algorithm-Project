def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for num in arr:
        count[num] += 1
    arr.clear()
    for i in range(len(count)):
        arr.extend([i] * count[i])
    return arr
