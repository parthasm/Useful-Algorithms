Single Source Shortest Path
========

Python implementations of Djikstra's algorithm and Bellman-Ford algorithm to solve the Single Source Shortest Path problem for a graph. 

http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm

All the versions calculate the shortest path distance of the vertex '1' to all the vertices and print the shortest distance to vertex '7'.

Input Format
========

Each row lists a vertex and all vertices connected to it, along with edge costs.
For example, a row: 

1	80,982	163,8164	170,26

indicates the vertex 1 is connected to the vertex 80 and the edge-cost of their edge is 982.
Similarly vertex 1 is connected to the vertices 163 and 170 with the edge-costs of their edges as 8164 and 26, respectively.
Please note that the graph in the 'Input.txt' file is undirected, although the Single Source Shortest Path problem is usually defined for directed graphs. However, both Bellman-Ford and Djikstra can be modified to solve this problem for undirected graphs. This is what has been done in this case. 

All the variants of Djikstra and Bellman-Ford are listed below:

##Djikstra_Dictionary_List.py

Graph Data Structure:

The Graph is stored as a dictionary with each source vertex v as key. The corresponding value is a list of tuples. Each tuple has 2 elements - the destination vertex w connected to v and the cost of the v-w edge. 

Traversal:

There is an outer while loop which runs as long as the number of processed vertices is less than V, the total number of vertices. The vertices (v)s which have been processed are traversed in the inner loop to find their incident vertex-cost pairs (w-e)s. If the vertex w is not yet processed, then the Djikstra score is calculated for it. Out of all the vertices w for all the vertices v, the vertex w with the minimum Djikstra score is selected.


Djikstra score = The previously computed shortest path distance to the vertex v + e


##Djikstra_Double_Dictionary.py

Graph Data Structure:

Instead of a dictionary-list, a nested dictionary is used. The Graph is stored as a dictionary with each source vertex v as key. But its value now is an inner dictionary, with each destination vertex w as key and edge-cost e as value.

Traversal:

Same as in Djikstra_Dictionary_List.py


##Djikstra_DD_Unprocessed.py

Graph Data Structure:

Similar to the Graph data structure Djikstra_Double_Dictionary.py, except roles of the source vertex and destination vertex are reversed, i.e, key of the outer dictionary is the destination vertex while key of the inner dictionary is the source vertex. This is because in this version of the algorithm( and in all the versions below ), we need to find all the relevant source vertices from a given destination  vertex. 

Traversal:

Instead of processed vertices, the focus of traversal is unprocessed vertices. The outer while loop runs as long as shortest-path-distances to one or more vertices are not calculated. The for loop inside it traverses over the vertices in the Graph which are yet unprocessed. For every unprocessed vertex w, it traverses its connected vertices. If the connected vertex v is already processed, the Djikstra score ( described above ) is calculated. In every iteration of the outer while loop, the vertex w with the minimum Djikstra score is selected and removed from the list of unprocessed vertices, while updating the shortest path from the source vertex to the newly-added vertex w.


##Djikstra_DD_Unprocessed_Heap.py

Graph Data Structure:

Same as in Djikstra_DD_Unprocessed.py

Traversal:

Here, the heap data strcuture is used. It stores all the unprocessed vertices with keys as their minimum Djikstra scores ( described above ). Thus the vertex with the minimum Djikstra score out of all the vertices in the heap can simply be popped from the heap.  For every such vertex w extracted from the heap, if it has edges to vertices v in the heap, then the Djikstra scores for these vertices v are recomputed. They are then swam up in the heap, if their scores have improved. The main functionality is performed by the DjikstraHeap() function in 'SSSP.py'.

##BellmanFord.py

Graph Data Structure:

Same as in Djikstra_DD_Unprocessed.py

Traversal:

A dynamic programming algorithm is used. It grows the number of edges allowed for minimum distance computation to every destination vertex at every step. There are 2 versions and the user can choose one - Naive and Optimized. The only difference is that in the opimized version once there is no improvement in the minimum distance-scores in one iteration of the outer for loop, it immediately stops, since the lack of improvement implies that the shortest-path distances have been found. The main functionality is performed by the BellmanFord() in 'SSSP.py'.

##SSSP.py

SSSP = Single Source Shortest Path. 
This file contains functions required to run Bellman-Ford - both naive and optmized versions and heap-based Djikstra's algorithm. 

##Observations:

The complexity of Bellman-Ford algorithm = O(m*n)

The complexity of heap-based version of Djikstra's algorithm = O(m*log(n))

Due to lower complexity, the time taken by the heap-based version of Djikstra's algorithm is less than one-fourth of the time taken by the naive version of  Bellman-Ford, even in a sparse graph with 200 vertices. Interestingly, the optimized version of Bellman-Ford takes the same time as the heap-based version of Djikstra, showing that clever optimizations may compensate for higher complexities,especially with small/medium-sized input. 

##Note:

m = #edges

n = #vertices
