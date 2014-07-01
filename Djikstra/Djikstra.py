fi = open('dijkstraData.txt')
#fi = open('test_case.txt')
graph={}
n=0
for line in fi:
    string = line.strip()
    vertex = string[:string.find('\t')]
    string = string[string.find('\t')+1:]
    connected_to=[]
    while string.find('\t')!=-1:
        v_el = string[:string.find('\t')]
        comma_index=v_el.find(',')
        connected_to.append([v_el[:comma_index],v_el[comma_index+1:]])
        string = string[string.find('\t')+1:]
    v_el=string        
    connected_to.append([v_el[:v_el.find(',')],v_el[v_el.find(',')+1:]])
    graph[vertex] = connected_to
    n+=1
#print graph    
#created a dictionary with each vertex as the key
#the value of the dictionary is a list containing all the adjacent vertices
#& their distances
fi.close()

dict_shortest_path={}
dict_shortest_path['1']=0
while True:
    minimum = 1000000
    for v in dict_shortest_path.keys():
        #print v
        dests= graph[v]
        for d in dests:
            w = d[0]
            w_not_in_d = dict_shortest_path.get(w,-1)
            if w_not_in_d==-1:
                sp = dict_shortest_path[v]+int(d[1])
                if sp < minimum:
                    minimum = sp
                    w_star = w
    dict_shortest_path[w_star]=minimum
    #print "hi", dict_shortest_path        
    if len(dict_shortest_path)==n:
        break
#print dict_shortest_path
print dict_shortest_path['7']

