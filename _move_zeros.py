"""
    move zeros

    send zeros to last part of arrays
    [False, 1, 5, 8, 3, 9, 0, True, 0, "1", "5", "7", 0] ==> [False, 1, 5, 8, 3, 9, True, '1', '5', '7', 0, 0, 0]
"""


def move_zeros(seq):
    result = list()
    zeros = 0
    for i in seq:
        if i == 0 and type(i) != bool:
            zeros += 1
        else:
            result.append(i)
    result.extend([0] * zeros)
    return result


print(move_zeros([False, 1, 5, 8, 3, 9, 0, True, 0, "1", "5", "7", 0]))
