"""
        [1, 3, 5, 6], 3 => 1
        [1, 3, 5, 6], 4 => 2
        [1, 3, 5, 6], 7 => 4
        [1, 3, 5, 6], 0 => 0
"""


def search_insert(arr, val):
    low = 0
    high = len(arr) - 1
    mid = high // 2

    while low <= high:

        if val > arr[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid

    return low


print(search_insert([2, 5, 7, 10, 12, 15, 17], 0))
