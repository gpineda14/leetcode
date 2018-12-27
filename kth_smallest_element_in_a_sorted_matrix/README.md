# 378. Kth Smallest Element in a Sorted Matrix #

**Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.**

## Understanding the problem ##

So given an matrix that has its individual rows in a sorted fashion, we want to find the kth smallest element in the array. The wording is a bit tricky because it sounds as though the whole matrix is already, but that is not the case. Only its individual rows and columns are sorted so we have to figure out a way to find the kth smallest value inside the matrix. We know the input is going to be a matrix which is a 2d array and an integer k that is between 1 and n^2. The integer k indicates the kth smallest integer we are looking for.

Given the input, we will return an integer. What comes to mind is implementing a heap. We can add the values provided by the matrix to the heap. Afterwards, we can pop values from the heap k times to get the result we want.

## Concrete Examples ##

Given [[1, 2, 3], [3, 4, 5]] and k = 2
return 2

Given [[10, 11, 12], [11, 12, 14], [15, 16, 17]] and k = 4
return 12

Given [[10, 11, 12], [11, 12, 14], [15, 16, 17]] and k = 8
return 16

Given [[1, 2, 3], [1, 2, 3], [1, 2, 3]] and k = 5
return 2

## Break it down ##

1. Create a list that will function as a heap
2. Iterate through the matrix, adding values to the newly created heap
3. Once we have the heap, we will pop values from it k times
4. We return the kth value
