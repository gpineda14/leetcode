# 46. Permutations #

**Given a collection of distinct integers, return all possible permutations.**

## Understanding the problem ##

We want to see how many distinct ways we can rearrange an array of integers. The given input is going to be a list of distinct integers so we do not have to worry about duplicate values in the list. The output should be a list of lists, where each list inside the parent list is a permutation.

Since we know the contents of the input list, we need to find ways to reorganize the list. Because we want to find all distinct combinations, we need to find a way to backtrack on the list. I think we are going to need a recursive helper function for this to work.

So the following data we need to store is :

a. a list to hold all permutations
b. the current permutation
c. a helper function to find permutations

## Concrete Examples ##

Given [], return []

Given [1, 2], return [[1, 2], [2, 1]]

Given [1, 2, 3], return
[
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1]
]

Given [1, 2, 3, 4], return
[
  [1, 2, 3, 4],
  [1, 3, 4, 2],
  [1, 4, 2, 3],
  [1, 2, 4, 3],
  [1, 3, 2, 4],
  [1, 4, 3, 2],
  []
], should have 24 permutations

## Break it down ##

1. Create a perm list to hold permutations
2. Create makePermutation function
  a. have it accept two arrays: one to hold current permutation and other to keep track of values that have not been included in current permutation yet
  b. base case: if len(currPerm) == len(initList), add currPerm to perm and return
  c. iterate through waitingList
  d. add ith value to currPerm
  e. remove ith value from waitingList
  f. run makePermutation recursively
3. Return perm
