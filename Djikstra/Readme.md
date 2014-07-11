Djikstra
========

A python implementation of the famous Djikstra's algorithm.

http://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

All the versions calculate the shortest path distance of the vertex '1' to all the vertices and print the shortest distance to vertex '7'.

Input Format
========

Each row lists a vertex and all vertices connected to it, along with edge costs.
For example, a row: 

1	80,982	163,8164	170,26

indicates the vertex 1 is connected to the vertex 80 and the edge-cost of their edge is 982.
Similarly vertex 1 is connected to the vertices 163 and 170 with the edge-costs of their edges as 8164 and 26, respectively.

All the numerous variants of Djikstra; with different data-structures and different traversals of vertices are listed below:

##Djikstra_Dictionary_List.py

The Graph is stored as a dictionary with each vertex as key. 

