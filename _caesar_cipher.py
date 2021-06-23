"""
جولیوس سزار از اطلاعات محرمانه خود با رمزنگاری با استفاده از رمزنگاری محافظت کرد.
رمز سزار هر حرف را با تعدادی حرف تغییر می دهد. اگر شیفت شما را ببرد
از انتهای الفبا گذشته ، فقط به جلو الفبا بچرخید.
در صورت چرخش 3 ، w ، x ، y و z به z ، a ، b و c ترسیم می شود.
------------------------------------------------------------------------------------------------
Julius Caesar protected his confidential information by encrypting it using a cipher.
Caesar's cipher shifts each letter by a number of letters. If the shift takes you
past the end of the alphabet, just rotate back to the front of the alphabet.
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.
------------------------------------------------------------------------
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""
from string import ascii_letters


def encrypt_str(string, key):
    alpha = ascii_letters
    result = " "

    for ch in string:
        if ch not in alpha:
            result += ch
        else:
            new_key = (alpha.index(ch) + key) % len(alpha)
            result += alpha[new_key]
    return result


def decrypt_str(string, key):
    key *= -1
    return encrypt_str(string, key)


def brute_force(string):
    alpha = ascii_letters
    key = 1
    result = ""
    brute_force_data = {}

    while key < len(alpha):
        result = decrypt_str(string, key)
        brute_force_data[key] = result
        result = ''
        key += 1
    return brute_force_data


print(encrypt_str('reza', 4))
print(decrypt_str('viDe', 4))
print(brute_force('viDe'))