Graph-Search
============

Python implementations of depth-first-search and breadth-first-search.

http://en.wikipedia.org/wiki/Depth-first_search

http://en.wikipedia.org/wiki/Breadth-first_search

For both BFS and DFS, the sequence in which the vertices are traversed is printed.

##Input Format


In all the input files 'test_case*.txt' , each row lists a vertex and all the vertices connected to it. For example, a row: 

5	193	156	102

indicates the vertex 5 is connected to the vertices 193, 156 and 102.



##Implementation Details

The graphs are implemented as dictionaries, where the key is a vertex and its corresponding value is the list of connected vertices. 


Depth-first Search is implemented in the recursive way. 

Possible Sources of Improvement:

a)Use of optimizer packages which enables efficient use of tail recursion in python 

b) Implementing DFS in another language where tail recursion is highly optimized by default, like Java.

c) An iterative, non-recursive implementation of DFS


