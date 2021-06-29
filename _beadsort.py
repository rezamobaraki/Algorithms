"""
    bead sort
        [3, 1, 7, 5, 10 ,11] ==> [1, 3, 5, 7, 10 ,11]
        1(3,1) 2(1,7) 3(7,5) 4(5,10)
"""


def bead_sort(sequence):
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError('sequence must be list of non-negative integers')

    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence


print(bead_sort([3, 1, 7, 5, 10, 11]))

"""
    [1, 3, 5, 4]
    1) 0(1, 3) => if 1 > 3 : ... else repeat 
    2) 1(3, 5) => if 3 > 5 : ... else repeat
    3) 2(5, 4) => if 5 > 4 : list[2] -= 5 - 4 ==> [1, 3, 4, 4] && list[2 + 1] += 5 - 4 ==>  [1, 3, 4, 5]   
"""

a = 2

