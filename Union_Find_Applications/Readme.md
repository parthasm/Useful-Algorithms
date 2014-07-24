Union-Find Applications
========

Python implementations of Kruskal's Minimum Spanning Tree algorithm and Single-Link Clustering algorithm 
using multiple variants of the Union-Find data structure and also without using the Union-Find.
Union-Find is also known as Disjoint-set data structure. 
The Kruskal implementations print the sum of edge-costs of the Minimum Spanning Tree. The Single-Link Clustering 
implementations print maximum-spacing when the number of clusters is 4.


http://en.wikipedia.org/wiki/Disjoint-set_data_structure

http://en.wikipedia.org/wiki/Single-linkage_clustering

http://en.wikipedia.org/wiki/Kruskal's_algorithm

http://en.wikipedia.org/wiki/Minimum_spanning_tree



##Input Format

In all the input text files,for each edge, there is a line in the text file listing the 2 connected vertices and the edge weight. For example, the line:

1 2 6807

indicates that vertex 1 is connected to vertex 2 with an edge of cost 6807.
The only exception is the 1st line which either lists the number of vertices and number of edges or 
only the number of vertices.

Please note: 

m = #edges

n = #vertices


The code files are described below:

##Kruskal_BFS.py

As per Kruskal's MST algorithm, the edges are sorted in ascending order and added to the MST one by one, if they do not form a cycle with the already added edges. The check for the cycle implies checking if there is already a path between the 2 vertices of the edge in question. This checking is done by Breadth-First-Search in this naive implementation of Kruskal's algorithm.

##Kruskal_Union_Find.py

The only difference with the above is the check for cycles. Here , it is done by the Union-Find Data structure. If the 2 vertices of the edge in question are part of the same connected component, it implies adding the edge will create a cycle. 

This program offers multiple flavors of Union Find for the user to choose from -

a) Quick Find

b) Quick Union

c) Quick Union with Path Compression

d) Weighted Quick Find

e) Weighted Quick Union

f) Weighted Quick Union with Path Compression

All of which are implemented in separate files, described below, after the description of the Single Link Clustering file.

##Single_Link_Clustering_Union_Find.py

This is a greedy algorithm in order to find maximum spacing, where spacing is the minimum distance between all pairs of vertices in 2 different clusters.It is almost same as Kruskal, except it stops when the number of connected components, (referred to as clusters in the context of this algorithm) is 4.

Similar to Kruskal's, it offers multiple flavors of Union Find.

A few points about Union Find before the descriptions of its variants.

a) Root -  any one vertex in a Connected Component/Cluster , by which the cluster is identified.

b) Find - An operation to find the root of a cluster, when any vertex of the cluster is given.

c) Union - An operation to coalesce 2 clusters are together.

d) Connected - An operation to check if 2 vertices belong to the same cluster

##Quick_Find.py

Here the find operation is just one array-access. However, this implies that when an union is performed between clusters A & B, all the vertices in the cluster B, need to have their roots changed, an operation of the order O(n)

##Quick_Union.py

Here during an union between A & B, the root of A is assigned as root of B. This implies constant time unions, but to find the root of a cluster, one has to keep traversing among the individual roots until a vertex is found which is its own root. If the cluster is imagined as a tree, it is an unbalanced one. Therefore, its height is of the order O(n). Hence the all operations are of the order O(n)(Even Union, because in union, the roots of the 2 clusters need to be found)

##Quick_Union_with_Path_Compression.py

Same as Quick Union, except all the vertices traversed on the way to find the root, are assigned the final root as its root in the array storing roots. This makes the tree structure almost flat. 

##Weighted_Quick_Find.py

Same as Quick Find, except that in the union operation, it is ensured that the vertices of the smaller cluster (and not the larger cluster ) have their roots changed. This implies that the cluster size at least doubles when the root of a vertex in it is changed. Thus 1 vertex can have its root changed only O(log (n)) times. For all union operations, the upper bound is therefore O(n*log (n)).

##Weighted_Quick_Union.py

Same as Quick Union, except that it is always the root vertex of the smaller cluster which has its root changed. 

##Weighted_Quick_Union_with_Path_Compression.py

Same as previous, also uses path compression as described before.


