
def partition(v, ini, fim):
    pivo = ini

    for i in range(ini+1, fim+1):
        if v[i] <= v[ini]:
            pivo += 1
            v[i], v[pivo] = v[pivo], v[i]
    v[pivo], v[ini] = v[ini], v[pivo]
    return pivo


def quickSort(v, ini, fim):
    if fim > ini:
        pivo = partition(v, ini, fim)
        quickSort(v, ini, pivo-1)
        quickSort(v, pivo+1, fim)

ex = [1, 23, 1, 2, 6, 67, 66, 6, 5, 4]

quickSort(ex, ex[0], len(ex)-1)
print ex
