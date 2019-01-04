# 39. Combination Sum #

**Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.**

## Understanding the problem ##

Given a list of integers and a target integer value, we want to see how many different ways we can make the target value using various integers in the list. The list will be a set so there will be no duplicate values, but we are allowed to use the same number multiple times. We also know that the list of values will be all be positive and the list of  combination of values cannot contain duplicate combinations.

We can try to find combinations by starting with the beginning of the list and incrementing that value until we reach a particular threshold. Once we reach a threshold we can move to the next value or be finished and push the newly created list of values into our solutions list.

We would need a set to hold all the unique combinations. We also need to figure out what the threshold will be for moving on to the next values.

## Concrete Examples ##

given [2, 3, 6, 7], 7
return [
  [7],
  [2, 2, 3]
]

given [2, 3, 5], 8
return [
  [2, 2, 2, 2],
  [2, 3, 3],
  [3, 5]
]

given [1, 2], 2
return [
  [1, 1],
  [2]
]

given [1, 2, 3], 3
return [
  [1, 1, 1].
  [1, 2],
  [3]
]

given [1, 2, 3, 4], 4
return [
  [1, 1, 1, 1],
  [1, 1, 2],
  [1, 3],
  [2, 2],
  [4]
]

given [1, 2, 3, 4, 5], 5
return [
  [1, 1, 1, 1, 1],
  [1, 1, 1, 2],
  [1, 1, 3],
  [1, 2, 2],
  [1, 4],
  [2, 3],
  [5]
]

## Break it down ##

1. create a list to hold all combinations
2. create a helper function that will find all combinations
  - append to array when target is 0
  - return if target is less than 0
  - iterate through the list from current index to end of candidates
    - append value in candidate at current index
    - subtract curr value from target and recursively call the function
    - pop the last value to reuse the curr list 
3. return combo list
