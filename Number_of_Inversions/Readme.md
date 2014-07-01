Number-Of-Inversions
====================

Definition - It is the number of pairs of places of a sequence where the elements on these places 
are out of their natural order.

Source: http://en.wikipedia.org/wiki/Inversion_%28discrete_mathematics%29

This repository contains the following components:

An algorithm to count the number of inversions in an array based on merge sort, coded in python. This code is present in 
in the file 'no__of_inversions.py'. 
 
An actual implementation of mergesort in python is in the file 'merge_sort.py'.
 
 The files 'IntegerArray_input.txt' and 'test_inv.txt' can serve as input to both the programs, 
 but the current implementations of both take the 1st file as input.
 
 'no__of_inversions.py' prints out the number of inversions, while 'merge_sort.py' requires 
 an output file where it prints all the numbers of the sequence in sorted order. 'IntegerArray_sorted.txt' 
 is this output file. 

Possible Sources of Improvement:

a)Use of optimizer packages which enables efficient use of tail recursion in python. 

b) Implementing the same algorithms in another language where tail recursion is highly optimized by default, like Java.

c) An iterative, non-recursive implementation of the same algorithms
