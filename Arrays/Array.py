def display(arr):
    print("[", end="")
    for i in arr:
        print(arr[i], end=" ")
    print(" ]")


def set_element(arr, index, number):
    arr[index] = number


def get_element(arr, index):
    return arr[index]


def linear_search(arr, key):
    for i in arr:
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, start, end, key):
    if start <= end:
        mid = (start + end) / 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            return binary_search(arr, start, mid - 1, key)
        else:
            return binary_search(arr, mid + 1, end, key)
    return -1


def reverse(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1
    return arr


def get_max_element(arr):
    max_element = arr[0]
    for i in arr:
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element


def get_min_element(arr):
    min_element = arr[0]
    for i in arr:
        if arr[i] < min_element:
            min_element = arr[i]
    return min_element


def check_if_sorted(arr):
    for i in arr:
        if arr[i] > arr[i + 1]:
            return False
    return True


def merge_sorted_arrays(arr1, arr2):
    merged_arr = []
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged_arr[k] = arr1[i]
            i = i + 1
        else:
            merged_arr[k] = arr2[j]
            j = j + 1
        k = k + 1
    if i < len(arr1):
        while i < len(arr1):
            merged_arr[k] = arr1[i]
            i = i + 1
            k = k + 1
    else:
        while j < len(arr2):
            merged_arr[k] = arr2[j]
            j = j + 1
            k = k + 1
    return merged_arr


def union_on_sorted_arrays(arr1, arr2):
    union_arr = []
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            union_arr[k] = arr1[i]
            i = i + 1
            if arr1[i] == arr2[j]:
                j = j + 1
        else:
            union_arr[k] = arr2[j]
            j = j + 1
        k = k + 1
    if i < len(arr1):
        while i < len(arr1):
            union_arr[k] = arr1[i]
            i = i + 1
            k = k + 1
    else:
        while j < len(arr2):
            union_arr[k] = arr2[j]
            j = j + 1
            k = k + 1
    return union_arr


def intersection_on_sorted_arrays(arr1, arr2):
    intersection_arr = []
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i = i + 1
        elif arr1[i] > arr2[j]:
            j = j + 1
        else:
            intersection_arr[k] = arr1[i]
            i = i + 1
            j = j + 1
        k = k + 1
    return intersection_arr


def set_diff_on_sorted_arrays(arr1, arr2):
    set_diff_arr = []
    i = 0
    j = 0
    k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            set_diff_arr[k] = arr1[i]
            i = i + 1
            k = k + 1
        elif arr1[i] > arr2[j]:
            j = j + 1
        else:
            i = i + 1
            j = j + 1
    while i < len(arr1):
        set_diff_arr[k] = arr1[i]
        i = i + 1
        k = k + 1
    return set_diff_arr
