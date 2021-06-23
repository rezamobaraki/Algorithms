"""
    Linear Time O(n)

"""

nums = [2, 16, 43, 68, 543, 7, 3, 27, 9, 5, 68, 354, 864, 65, 1, 7, 983, 6, 0, 4, 23, 65, ]


def show(list_nums):
    max_num = list_nums[0]
    for num in list_nums:
        if num > max_num:
            max_num = num
    return max_num


print(show(nums))
