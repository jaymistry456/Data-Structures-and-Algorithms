def heapify(arr, n, i):
    largest = i
    left_child = i * 2 + 1
    right_child = i * 2 + 2
    if left_child < n and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < n and arr[right_child] > arr[largest]:
        largest = right_child
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Building max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extracting elements from the max heap
    for i in range(n - 1, 0, -1):
        # Swapping the largest element with the end index element of the array
        arr[i], arr[0] = arr[0], arr[i]
        # Calling heapify on the remaining elements except the last swapped
        heapify(arr, i, 0)
