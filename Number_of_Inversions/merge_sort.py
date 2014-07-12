def merge(li):
    length = len(li)
    if length==1:
        return li
    le_li = li[:length/2]
    ri_li = li[length/2:]
    le_li = merge(le_li)
    ri_li = merge(ri_li)
    sorted_li=[]
    le_itr=0
    ri_itr=0
    while True:
        if le_li[le_itr]>ri_li[ri_itr]:
            sorted_li.append(ri_li[ri_itr])
            ri_itr+=1
            if ri_itr==len(ri_li):
                sorted_li.extend(le_li[le_itr:])
                return sorted_li
            
        else:
            sorted_li.append(le_li[le_itr])
            le_itr+=1
            if le_itr==len(le_li):
                sorted_li.extend(ri_li[ri_itr:])
                return sorted_li


import time
start_time = time.time()

import sys
sys.setrecursionlimit(10000)
fi = open('IntegerArray_input.txt')
li = []
for line in fi:
    li.append(int(line))       
li = merge(li)
fo = open('IntegerArray_sorted.txt','w')
for num in li:
    fo.write(str(num)+"\n")
fi.close()
fo.close()

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"

###Tail-Recursion optimizations absent in python,
###therefore , recursive algos in python not advisable
