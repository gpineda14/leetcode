# 215. Kth Largest Element in an Array #

**Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.**

## Understanding the problem ##

So given an array that is not sorted, we want to return the kth largest number in the list.

The input given is an array of numbers only and a number k that indicates position. The output an integer that is the kth largest value.

We can assume k won't be larger than the length of the array and we know only integers will in the list.

Seeing as we want the kth largest number, a heap looks like a good data structure for the problem.

## Concrete Examples ##

Given ls = [1, 2] and k = 2
return 1

Given ls = [1, 1, 1, 1, 1] and k = 1
return 1

Given ls = [4, 7, 12, 5, 8, 0] and k = 6
return 0

Given ls = [100, 57, 343, 57] and k = 1
return 343

Given ls = [] and k = 1
return []

Given ls = [1] and k = 2
return 1

Given ls = [30, 30, 30, 25] and k = 2
return 30

## Break it down ##

Okay the first thing I need to do is convert the list into a min-heap.

From there, we will be popping min-values (which are actually max values) until we get the kth value. Once we reach the kth value, we need to negate the value and return it.  
