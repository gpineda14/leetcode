# 718. Maximum Length of Repeated Subarray #

**Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.**

## Understand the problem ##

We are given two arrays and are asked to return the length of the largest subarray that is present in both arrays. We are asked to output the size of the largest common subarray.

It is important to note that both input arrays do not have to be the same size. We have to figure out a way to keep track of all common values between A and B and from there we can search through those common points through iteration and determine the largest value from there.

## Concrete Examples ##

Given [1, 1, 1, 1, 1, 4, 5], [4, 5, 7, 1, 1, 1, 1, 1]
return 5

Given [], [1, 2]
return 0

Given [3, 4, 5], [5, 4, 3]
return 0

Given [1, 2, 3, 2, 1], [3, 2, 1]
return 3

Given [4, 5, 6], [4, 5, 6, 4, 5, 6]
return 3

## Break it down ##

1. create a default dictionary to keep track of all numbers and their indices in A
2. create a max_len variable to keep track of max value
3. iterate through array B 
  - if elem in B is in A, then we begin a second iteration of the indices
  - create a variable called curr_max to keep track of local max
  - we keep track of index of elem in B and curr index from A and begin moving the pointer forward until B[elem] != A[curr].
  - compare max_len with curr_max, if curr_max > max_len, set max_len = curr_max
4. return max_len
