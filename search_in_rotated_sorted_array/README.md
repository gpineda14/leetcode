# 33. Search in Rotated Sorted Array #

**Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).**

## Understand the problem ##

The given input is a list of integers that are sorted. The difference however is that the list was rotated on a pivot. We are also given a target and are asked to return the index of the target in O(log n) time.

## Concrete Examples ##

Given [4,5,6,7,0,1,2], 0
return 4

Given [7,0,1,2,3,4,5,6], 3
return 4

Given [5,6,7,1,2,3,4], 3
return 5

Given [7,9, 10, 2, 3, 5], 10
return 2

Given [5,7,9,1,3], 3
return 4

Given [9,1,3,4], 4
return 3

## Break it down ##

1. Use binary search to find the rotate_index
2. using the rotate_index, we do a binary search from 0 to rotate_index or rotate_index to n - 1
