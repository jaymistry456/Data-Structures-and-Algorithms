def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i = i + 1
        while i <= j and arr[j] > pivot:
            j = j - 1
        if j < i:
            break
        else:
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[low] = arr[low], arr[j]
    return j


def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)
        quick_sort(arr, low, partition_index - 1)
        quick_sort(arr, partition_index + 1, high)
