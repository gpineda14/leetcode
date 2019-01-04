# 565. Array Nesting #

**A zero-indexed array A of length N contains all integers from 0 to N-1. Find and return the longest length of set S, where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of element A[i] of index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By that analogy, we stop adding right before a duplicate element occurs in S.**

## Understanding the problem ##

We want to iterate through the list and see what is the list length of values we can iterate without reaching a previous value. The way we iterate through a list will be slightly different. We begin with index 0 and whatever value is at index 0 will be the index of the next value we search. We keep doing that until we reach the starting value again. The input will be a list of length N and the list will contain ALL values from 0 to N - 1. We will return an integer that indicates the largest length of the set of values that do not repeat. We can find this by iterating through the list and also keeping track of its size. Every time we find a repeat, we begin the search again but begin at the next index.

## Concrete Examples ##

Given [1, 2, 3, 0]
return 4

Given [0, 2, 1, 3]
return 2

Given [5, 0, 1, 2, 3, 4]
return 6

Given [4, 3, 2, 1, 0]
return 2

## Break it down ##

1. create an array of size n and fill with False
2. create an ans variable and set to 0
3. iterate through the numbers in nums
  - set value at i to start
  - create a separate while loop with start != nums[i] as break
    - create a count variable and increment by 1
    - set start = nums[start]
    - set arr[nums] = True
  - set ans to the max of ans and count 
4. return ans
