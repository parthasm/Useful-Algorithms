
import time
start_time = time.time()
fi = open('Input.txt')
#fi = open('test_case.txt')
Graph={}
n=0
for line in fi:
    li = line.split()
    v = int(li[0])
    connected_to=[]
    for we in li[1:]:
        we = we.split(',')
        connected_to.append((int(we[0]),int(we[1])))
    Graph[v] = connected_to
    n+=1
#print Graph    
#created a dictionary with each vertex as the key
#the value of the dictionary is a list containing all the adjacent vertices
#& their distances
fi.close()

dict_shortest_path={}
dict_shortest_path[1]=0
while True:
    minimum = 1000000
    for v in dict_shortest_path.keys():
        #print v
        dests= Graph[v]
        for d in dests:
            w = d[0]
            w_not_in_d = dict_shortest_path.get(w,-1)
            if w_not_in_d==-1:
                sp = dict_shortest_path[v]+d[1]
                if sp < minimum:
                    minimum = sp
                    w_star = w
    dict_shortest_path[w_star]=minimum
    #print "hi", dict_shortest_path        
    if len(dict_shortest_path)==n:
        break
#print dict_shortest_path
print dict_shortest_path[7]

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"

