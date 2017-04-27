def reduc(a):
    a = list(a)
    for x in a:
        if x in a and a.count(x) > 1:
            a.remove(x)
            a.remove(x)
    a = "".join(a)
    if a:
        return a
    else:
        return 'Empty String'

reduc('aaaammmeeeeaa')


def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)


def red(array, rs):
    array = list(array)
    if allUnique(array) and len(array) == 0:
        if rs:
            return ''.join(rs)
        else:
            return 'Empty String'
    elif len(array) >= 1:
        v = array.pop()
        if v in array:
            array.remove(v)
        else:
            rs.insert(0, v)

    return red(array, rs)

red('zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh', [])


def removeRepeats(S):
    LS = list(S)
    i = 0
    while i < len(LS)-1:
        if LS[i] == LS[i+1]:
            del LS[i]
            del LS[i]
            i = 0
            if len(LS) == 0:
                return 'Empty String'
        else:
            i += 1
    return ''.join(LS)
removeRepeats('zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh')


asMariasEstaoLegais


def count_words_in_camelcase(word):
    word = list(word)
    i = 1
    for x in word:
        if x.isupper():
            i += 1
    return i

count_words_in_camelcase('asMariasEstaoLegais')