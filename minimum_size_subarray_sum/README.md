# 209. Minimum Size Subarray Sum #

**Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.**

## Understand the problem ##

We are given an array of values that are positive and an integer s. The s is going to be a number that we are trying to sum up using a subarray. We want to output an integer that is the length of the **smallest** subarray.

So, in essence, we want to find the starting index and ending index of the subarray that equates to the sum. We also want the smallest array possible.

## Concrete Examples ##

given [1,2,3,4,5], 5
return 1

given [1,2,3,4,5], 6
return 2

given [1,2,3,4,5], 1
return 1

given [6,5,8,0,1,2], 3
return 1

given [6,5,8,0,1,2], 10
return 2

given [3,2,3,2,3], 5
return 2

given [9,1,3,4,3,2], 7
return 1

given [9,1,3,4,3,2], 10
return 2

## Break it down ##

1. create two pointers, start and end
  - create global_min
2. iterate through the array, fixing start at i
  - start = arr[i]
  - count = 1
3. iterate through the array again from i + 1 to end
  - add current value at index j to start
  - increment count by 1
  - if start > sum,
    - get the min of count and global_min
4. return global_min

## Refactor ##

We create a couple variable:
- n = len(nums)
- min_len = sys.maxsize (to keep track of min)
- left = 0, index of start of subarray
- sum = 0, total sum of array elements

We first iterate through the array elements adding every element to the sum variable.

In a nested loop, while sum >= s, we get compare min_len and i + 1 - left and set the smaller one to min_len. Afterwards we subtract nums[left] from sum and increment left.

Afterwards we return the min_len if min_len does not equal to sys.maxsize, else we return 0.
