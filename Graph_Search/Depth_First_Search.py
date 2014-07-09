def dfs(seen,v):
    seen.append(v)
    vc = Graph[v]
    if len(vc)>0:
        for v1 in vc:
            if v1 not in seen:
                dfs(seen,v1)
    
import time
start_time = time.time()


fi = open('test_case.txt')
Graph={}
for line in fi:
    li = line.split()
    Graph[li[0]]=li[1:]

#created a dictionary with 1st vertex of each row as key and the list containing the rest connected vertices
#as value
fi.close()
    
#print graph    

import sys
sys.setrecursionlimit(10000)
seen=[]
dfs(seen,'1')
print seen


print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
