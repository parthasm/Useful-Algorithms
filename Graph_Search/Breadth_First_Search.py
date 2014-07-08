
import time
start_time = time.time()

#fi = open('test_case_bfs.txt')
fi = open('test_case_bfs_2.txt')
Graph={}
for line in fi:
    li = line.split()
    Graph[li[0]]=li[1:]
        
#created a list with each row as an item in the list
#the rows themselves are lists with the 1st element as the vertex
#the 2nd element of the row is a list containing all the adjacent vertices
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
