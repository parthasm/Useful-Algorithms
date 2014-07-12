def inv_count_and_merge(li):
    length = len(li)
    if length==1:
        return [0,li]
    le_li = li[:length/2]
    ri_li = li[length/2:]
    le_li = inv_count_and_merge(le_li)
    count_left = le_li[0]
    le_li = le_li[1]
    ri_li = inv_count_and_merge(ri_li)
    count_right = ri_li[0]
    ri_li = ri_li[1]
    sorted_li=[]
    le_itr=0
    ri_itr=0
    count = count_left+count_right
    while True:
        if le_li[le_itr]>ri_li[ri_itr]:
            sorted_li.append(ri_li[ri_itr])
            ri_itr+=1
            count+=(len(le_li)-le_itr)
            if ri_itr==len(ri_li):
                sorted_li.extend(le_li[le_itr:])
                return [count,sorted_li]
            
        else:
            sorted_li.append(le_li[le_itr])
            le_itr+=1
            if le_itr==len(le_li):
                sorted_li.extend(ri_li[ri_itr:])
                return [count,sorted_li]


import time
start_time = time.time()


import sys
sys.setrecursionlimit(10000)
fi = open('IntegerArray_input.txt')
#fi = open('test_inv.txt')
li = []
for line in fi:
    li.append(int(line))       
final_count = inv_count_and_merge(li)[0]
print final_count
fi.close()

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"

###Tail-Recursion optimizations absent in python,
###therefore , recursive algos in python not advisable
