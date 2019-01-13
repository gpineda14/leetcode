# 15. 3 Sum #

**Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.**

## Understand the problem ##

Given an array of numbers, we want to return a list of triplets that if summed up together would equal 0. The list of triplets must not contain any duplicate triplets. We also know the input of arrays is not sorted. We are to output a list of triplets. The input array can have negative and positive numbers. The output is going to be a list of lists (of which contain three elements). We can find the output by iterating through all possible combinations and adding combinations that equate to zero to our result list.

## Concrete Examples ##

given [1, 0, -1]
return [[1, 0, -1]]

given [1,1]
return []

given [1, 2, 0, -2, -1]
return [[1,0,-1],[2,0,-2]]

given [1,1,1,1,0,-1]
return [[1,0,-1]]

given [5,4,0,1,-2,-2]
return [[4,-2,-2]]

## Break it down ##

1. Create solutions list to keep track of combinations
2. nested for loop
  - iterate from i to len(nums)
  - iterate from j = i + 1 to len(nums)
  - iterate from k = j + 1 to len(nums)
  - if nums[i] + nums[j] + nums[j] == 0, add to solutions

This would give us a time complexity of O(n^3)

## Refactor ##

We can reduce the time complexity by sorting the array first

1. sort the array
2. fix the first number at i
3. create two pointers, fix the first one at i + 1 and the second at the end
4. if sum in current values is less than 0, then increment left pointer
5. else decrement right pointer
6. return array of triplets
