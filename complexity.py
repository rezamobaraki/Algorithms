"""
    Complexity
        Time    Space

    Big O Notation
"""

nums = [2, 4, 6, 8, 10, 12, 14]


def show(num_list, element):
    for index, num in enumerate(num_list):
        if element == num:
            return index


def show2(num_list, element):
    for i in num_list:
        if i == element:
            return num_list.index(i)


print(show(nums, 4))
print(show2(nums, 4))
