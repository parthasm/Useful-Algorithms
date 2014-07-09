
import time
start_time = time.time()

#fi = open('test_case_bfs.txt')
fi = open('test_case.txt')
Graph={}
for line in fi:
    li = line.split()
    Graph[li[0]]=li[1:]
        
#created a dictionary with 1st vertex of each row as key and the list containing the rest connected vertices 
#as value
fi.close()


from collections import deque
q = deque([])
q.append('1')
bfs = []
while len(q)!=0:
    st = q.popleft()
    bfs.append(st)
    vc = Graph[st]
    for v in vc:
        if not ((v in bfs) or (v in q)):
            q.append(v)
            
print bfs

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
