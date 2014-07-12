def quicksort_median(li):
    length = len(li)
    if length < 2:
        return li

    n1 = li[0]
    mid=0
    if length%2==1:
        n2 = li[length/2]
        mid = length/2
    else:
        n2 = li[(length/2)-1]
        mid = (length/2)-1
    n3 = li[length-1]

    if (n2 <= n1 and n2 >= n3) or (n2 >= n1 and n2 <= n3):
        temp = li[0]
        li[0]=li[mid]
        li[mid]=temp
    elif (n3 <= n1 and n3 >= n2) or (n3 >= n1 and n3 <= n2):
        temp = li[0]
        li[0]=li[length-1]
        li[length-1]=temp
    


    
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
    left_list = quicksort_median(li[:i-1])
    right_list = quicksort_median(li[i:])
    
    final=[]
    final.extend(left_list)
    final.append(pivot)
    final.extend(right_list)
    return final

import time
start_time = time.time()

import sys
sys.setrecursionlimit(10000)
fi = open('Input.txt')
li = []
for line in fi:
    li.append(int(line))       
li = quicksort_median(li)
fo = open('Output.txt','w')
for num in li:
    fo.write(str(num)+"\n")
fi.close()
fo.close()

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"

###Tail-Recursion optimizations absent in python,
###therefore , recursive algos in python not advisable

