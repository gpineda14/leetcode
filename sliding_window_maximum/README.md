# 239. Sliding Window Maximum #

**Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.**

## Understand the problem ##

We are given an array of numbers and an integer k. The integer k indicates the size of the window we get to view as we find the max value in the window. The window moves to the right by one. We are to return the max of every window in an array. We can do this by slicing the array with the help of two pointers that indicate the beginning and ending of an array.

At every window, we find the max of the current array slice and add it to the max_window array.

## Concrete Examples ##

Given [1,3,-1,-3,5,3,6,7], 3
return [3,3,5,5,6,7]

Given [1,2,3,4,5,6], 6
return [6]

Given [1,1,1,1,1], 2
return [1,1,1,1]

## Break it down ##

1. create two pointers, i = 0 and j = k
2. create max_window list
3. iterate through nums while i < len(nums) and j < len(nums) + 1
  - append the max of subarray from i to j to max_window
  - increment i
  - increment j
4. return max_window 
