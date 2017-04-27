# Caesar Cipher
def shift_position(shift, letter):
    if shift > 90 and letter.isupper():
        shift -= 26
    elif shift > 122 and letter.islower():
        shift -= 26
    return shift


def encrypt(v, k):

    v = map(
        lambda x: chr(
            shift_position(ord(x) + k % 26, x)) if x.isalpha() else x, v)
    return ''.join(v)
