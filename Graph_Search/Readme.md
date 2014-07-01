Graph-Search
============

Python implementations of depth-first-search and breadth-first-search.

http://en.wikipedia.org/wiki/Depth-first_search

http://en.wikipedia.org/wiki/Breadth-first_search

The graphs are implemented as lists, where one element of a list is a 2-element list.
The 1st element is the vertex(a number), 
The 2nd element is a list of edges.


Depth-first Search is implemented in the recursive way. 

Possible Sources of Improvement:

a)Use of optimizer packages which enables efficient use of tail recursion in python 

b) Implementing DFS in another language where tail recursion is highly optimized by default, like Java.

c) An iterative, non-recursive implementation of DFS

d) Instead of a list, graph can be implemented as a dictionary, with the vertex as key and list of edges as value.

