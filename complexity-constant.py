"""
    Constant Time O(1)
"""

nums = [3, 2, 4, 6, 8, 10, 12, 14]


def show(list_nums):
    if list_nums[0] % 2 == 0:
        return "Even"
    return "Odd"


print(show(nums))
