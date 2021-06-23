"""
    Logarithm Time O(log n)

    solution : binary search
"""

nums = [1, 2, 4, 6, 8, 10, 12, 14]


def show(list_nums, element):
    for num in list_nums:
        if num == element:
            return list_nums.index(num)


print(show(nums,10))
