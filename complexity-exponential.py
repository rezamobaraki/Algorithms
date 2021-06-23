"""

    Exponential Time O(3^n) O(2^n) . . .

"""

from itertools import chain, combinations


def subset(iterable):
    iterable_list = list(iterable)
    return chain.from_iterable(combinations(iterable_list, r) for r in range(len(iterable_list) + 1))

print(list(subset(['a','c','b'])))
