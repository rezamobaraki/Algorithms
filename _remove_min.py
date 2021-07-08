"""
    remove min
    [4, 5, 2, 8, -2, 5, 1, 9] => -2
"""


def remove_min(stack):
    storage_stack = []

    if len(stack) == 0:
        return stack

    _min = stack[0]
    # _min = stack.pop()
    # stack.append(_min)
    for i in range(len(stack)):
        val = stack.pop()
        if val <= _min:
            _min = val
        storage_stack.append(val)
    for i in range(len(storage_stack)):
        val = storage_stack.pop()
        if val != _min:
            stack.append(val)
    return stack, _min


print(remove_min([4, 5, 2, 8, -2, 5, 1, 9]))
