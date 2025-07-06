# Quicksort algorithm implementation in Python Way 1
def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if e - s + 1 <= 1:
        return arr
    
    pivot = arr[e]
    left = s

    for i in range(s, e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left += 1
    
    arr[e] = arr[left]
    arr[left] = pivot

    quickSort(arr, s, left - 1)
    quickSort(arr, left + 1, e)
    return arr




# Quicksort algorithm implementation in Python Way 2
def quickSort(arr: list[int], s: int, e: int) -> list[int]:
    if s < e:
        p = partition(arr, s, e)
        quickSort(arr, s, p - 1)
        quickSort(arr, p + 1, e)
    return arr

def partition(arr: list[int], s: int, e: int) -> int:
    pivot = arr[e]
    i = s
    for j in range(s, e):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[e] = arr[e], arr[i]
    return i

