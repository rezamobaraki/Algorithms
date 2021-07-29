"""
    two sum
    [2, 6, 11, 15], 18 =>[2, 3]

"""


def two_sum(numbers, target):
    p1 = 0
    p2 = len(numbers) - 1

    while p1 < p2:
        s = numbers[p1] + numbers[p2]
        if s == target:
            return [p1, p2]
        elif s > target:
            p2 = p2 - 1
        else:
            p1 = p1 + 1


print(two_sum([3, 6, 11, 15], 26))
