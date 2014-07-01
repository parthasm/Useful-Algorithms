def quicksort_first(li):
    length = len(li)
    if length < 2:
        return li
    pivot = li[0]
    i = 1#right cell of the border inside partitioned cells
    #dividing numbers less than pivot on the left to the numbers
    #greater than pivot on the right
    j = 1#right cell of the border separating partitioned cells(left)
    #from non-partitioned cells(right)
    while j < length:
        if li[j]<pivot:
            temp = li[i]
            li[i]=li[j]
            li[j]=temp
            i+=1
        j+=1            
    temp = li[0]
    li[0]=li[i-1]
    li[i-1]=temp        
    left_list = quicksort_first(li[:i-1])
    right_list = quicksort_first(li[i:])

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

