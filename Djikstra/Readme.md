Djikstra
========

A python implementation of the famous Djikstra's algorithm.

http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

All the versions calculate the shortest path distance of the vertex '1' to all the vertices and print the shortest distance to vertex '7'.

Input Format
========

In the files 'dijkstraData.txt' and 'test_case.txt', each row lists a vertex and all vertices connected to it, along with edge costs.
For example, a row: 

1	80,982	163,8164	170,26

indicates the vertex 1 is connected to the vertex 80 and the edge-cost of their edge is 982.
Similarly vertex 1 is connected to the vertices 163 and 170 with the edge-costs of their edges as 8164 and 26, respectively.

All the numerous variants of Djikstra; with different data-structures and different traversals of vertices are listed below:

##Djikstra_Dictionary_List.py

Graph Data Structure:

The Graph is stored as a dictionary with each vertex v as key. The corresponding value is a list of tuples. Each tuple has 2 elements - the vertex w connected to v and the cost of the v-w edge. 

Traversal:

There is an outer while loop which runs as long as the number of processed vertices is less than V, the total number of vertices. The vertices (v)s which have been processed are traversed in the inner loop to find their incident vertex-cost pairs (w-e)s. If the vertex w is not yet processed, then the Djikstra score is calculated for it. Out of all the vertices w for all the vertices v, the vertex w with the minimum Djikstra score is selected.


Djikstra score = The previously computed shortest path distance to the vertex v + e


##Djikstra_Double_Dictionary.py

Graph Data Structure:

Instead of a dictionary-list, a nested dictionary is used. The Graph is stored as a dictionary with each vertex v as key. But its value now is an inner dictionary, with each connected vertex w as key and edge-cost e as value.

Traversal:

Same as in Djikstra_Dictionary_List.py


##Djikstra_DD_Unprocessed.py

Graph Data Structure:

Same as in Djikstra_Double_Dictionary.py

Traversal:

Instead of processed vertices, the focus of traversal is unprocessed vertices. The outer while loop runs as long as shortest-path-distances to one or more vertices are not calculated. The for loop inside it traverses over the vertices in the Graph which are yet unprocessed. For every unprocessed vertex w, it traverses its connected vertices. If the connected vertex v is already processed, the Djikstra score ( described above ) is calculated. In every iteration of the outer while loop, the vertex w with the minimum Djikstra score is selected and removed from the list of unprocessed vertices, while updating the shortest path from the source vertex to the newly-added vertex w.


##Djikstra_DD_Unprocessed_Heap.py

Graph Data Structure:

Same as in Djikstra_Double_Dictionary.py

Traversal:

Here, the heap data strcuture is used. It stores all the unprocessed vertices with keys as their minimum Djikstra scores ( described above ). Thus the vertex with the minimum Djikstra score out of all the vertices in the heap can simply be popped from the heap.  For every such vertex w extracted from the heap, if it has edges to vertices v in the heap, then the Djikstra scores for these vertices v are recomputed. They are then swam up in the heap, if their scores have improved. 
##Heap.py

An implementation of the heap data structure. This is the same heap implementation used in Prim's algorithm. 



##Note:

'Djikstra_DD_Unprocessed_Heap.py' takes around 20% of the time of the other versions, due to a lower worst-time complexity.

The complexity of Djikstra's algorithm in 'Djikstra_DD_Unprocessed_Heap.py' = O(m*log(n))

The complexity of Djikstra's algorithm in the other versions = O(m*n)



where,

m = #edges

n = #vertices
