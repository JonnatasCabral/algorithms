#!/usr/bin/ruby
def  insertionSort(ar, ctn)
    l = ctn - 1
    for i in 1..l
        ref = ar[i]
        j = i - 1
        while ref < ar[j] && j >= 0
            ar[j + 1] = ar[j]
            j = j-1
        end
        ar[j+1] = ref
        puts ar.join(' ')
    end
end
cnt = 6
ar = [10, 2, 52, 15, 4, 99]
insertionSort(ar, cnt)
