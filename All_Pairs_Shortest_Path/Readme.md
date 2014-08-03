All Pairs Shortest Path
======================

This problem can be solved by several ways - listed here are python implementations of Bellman-Ford algorithm run n times, Floyd-Warshall algorithm and Johnsons Algorithm. All the source files print the minimum distance among all the shortest path distances for every pair of vertices. Besides, all of them quickly identify a negative cycle and exit if one is present. 

http://en.wikipedia.org/wiki/Shortest_path_problem#All-pairs_shortest_paths

http://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm

http://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm

http://en.wikipedia.org/wiki/Johnson's_algorithm

##Input Format

In all the input files, the 1st line indicates the number of vertices and edges, respectively. The other lines describe an edge - listing the 2 connected vertices and the edge weight/cost. For example, the line:

4 1 -2

indicates that there is an edge from source vertex 4 to destination vertex 1 with cost -2. 


The code files are described below:

m = number of edges

n = number of vertices

##BellmanFord_All_Pairs.py

The idea is to run the BellmanFord function of SSSP.py (in the folder Single_Source_Shortest_Path) with each vertex in the graph serving as a source vertex. Since Bellman-Ford's runtime complexity is O(m*n) and there are 'n' vertices, this yields a resultant runtime complexity of O(m*(n^2)). It exits once the shortest path distances stop improving. 

##FloydWarshall.py

This is a dynamic programming algorithm whose complexity is O(n^3)

##Johnsons.py

The idea is to run the Bellman-Ford once to identify certain weights for every vertex. These weights are then used to reweight connecting edges, in order to make all edges non-negative. This enables Djikstra's algorithm to be run n times for n vertices. If the heap-based version of Djikstra's algorithm is used( simple heap, not Fibonacci Heap), the complexity is O(m*n*log(n))


More test-cases available here:

https://www.dropbox.com/sh/gasneang7m138eo/AABTAbOyRIRdVyWMmqDkcZwWa

Note: 
Floyd-Warshall's algorithm turned out to be the slowest, with a graph of 1000 vertices and 47978 edges ( moderately dense)  although it's complexity is better than all-pair Bellman-Ford for dense graphs. In fact, Bellman-Ford only took around 22.5% of the time of Floyd-Warshall. The pre-mature exit strategy of Bellman-Ford is perhaps the cause of this superior performance in practice. Johnson's algorithm, with its best run-time, trumps both of them, taking only around 7% of the time of Floyd-Warshall.
