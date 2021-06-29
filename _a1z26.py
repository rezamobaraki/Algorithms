"""
    a1z26
        reza <===> [114, 101, 122, 97]

"""


def encode(plain):
    return [ord(elm) - 92 for elm in plain]


print(encode("reza"))


def decode(plain):
    return "".join(chr(elm + 92) for elm in plain)


print(decode([22, 9, 30, 5]))