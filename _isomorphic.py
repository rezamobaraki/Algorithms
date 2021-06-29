"""

    is isomorphic
        foo, bar => False
        foo, bee => True
        fow, bee => True

        {f:b, o:e, w:e} (b, e, e)
"""


def is_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    dct = {}
    set_values = set()
    for i in range(len(str1)):
        if str1[i] not in dct:
            if str2[i] in set_values:
                return False
            dct[str1[i]] = str2[i]
            set_values.add(str2[i])
        else:
            if dct[str1[i]] != str2[i]:
                return False
    return True


print(is_isomorphic("foo", "baa"))
