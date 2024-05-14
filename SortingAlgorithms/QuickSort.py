def partition(arr, start, end):
    pivot = arr[end]
    partition_index = start
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
            partition_index = partition_index + 1
    pivot, arr[partition_index] = arr[partition_index], pivot
    return partition_index


def quick_sort(arr, start, end):
    if start < end:
        partition_index = partition(arr, start, end)
        quick_sort(arr, start, partition_index - 1)
        quick_sort(arr, partition_index + 1, end)
