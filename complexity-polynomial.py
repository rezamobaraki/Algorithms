"""

    Polynomial Time O(n^3) O(n^2) . . .

"""

nums = [2, 16, 43, 68, 543, 7, 3, 27, 9, 5, 68, 354, 864, 65, 1, 7, 983, 6, 0, 4, 23, 65, ]


def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break
    return collection


print(bubble_sort(nums))
