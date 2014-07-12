Randomized-Contraction-Algorithm
================================

An implementation of the randomized contraction algorithm in python to compute number of Minimum cuts in a graph.

##Input Format

In all the input files , each row lists a vertex and all the vertices connected to it. For example, a row:

5 193 156 102

indicates the vertex 5 is connected to the vertices 193, 156 and 102.

##Description of individual files:

'Randomized_Contraction_algo_dictionary.py' - The python source file where the graph is implemented as a python dictionary.

'Randomized_Contraction_algo_list.py' - The python source file where the graph is implemented as a python list.

'kargerMinCut.txt' - The input file

'test_case.txt' - The toy example input file, used as a test case.

Comments:
The dictionary implementation is supposed to be faster since it removes the iterations over the graph 
to find a particular vertex. However, the graph in 'kargerMinCut.txt' is too small to create a huge difference
in the time taken between the dictionary implementation and the python implementation.
