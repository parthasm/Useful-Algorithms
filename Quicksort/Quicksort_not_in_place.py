def quicksort_first(li):
    from collections import deque
    length = len(li)
    if length < 2:
        return li
    pivot = li[0]
    partitioned=deque([])
    partitioned.append(pivot)
    for n in range(1,length):
        if li[n]>pivot:
            partitioned.append(li[n])
        else:
            partitioned.appendleft(li[n])
            
    partitioned = list(partitioned)
    rank_pivot = partitioned.index(pivot)
    left_list = quicksort_first(partitioned[:rank_pivot])
    right_list = quicksort_first(partitioned[rank_pivot+1:])

    final=[]
    final.extend(left_list)
    final.append(pivot)
    final.extend(right_list)
    return final

import sys
sys.setrecursionlimit(10000)
fi = open('Input.txt')
li = []
for line in fi:
    li.append(int(line))       
li = quicksort_first(li)
fo = open('Output.txt','w')
for num in li:
    fo.write(str(num)+"\n")
fi.close()
fo.close()
###Tail-Recursion optimizations absent in python,
###therefore , recursive algos in python not advisable
