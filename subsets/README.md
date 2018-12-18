# 78. Subsets #

**Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.**

## Understanding the problem ##

Given a list of nums, we want to return the powerset of the set of numbers. This means we will return all unique combinations. Some things to notice is that the following is considered equal [1, 2] == [2, 1]. This means order does not matter, if it is the same set of numbers, then we have a subset.

We also see that the empty set is also a valid subset. We also know the whole set of numbers is also a subset. We can easily determine the subsets by hand by scanning through the list and pairing them.

If we were to do this by hand, we can add the empty set to the list of subsets and use an count to keep track of the current size of subsets we are looking for.

We will need a list to keep track of all the subsets and we need to figure out how to iterate and create subsets of size 1 to n - 1.

# Concrete Examples #

Given [1, 2, 3], return
[[], [1], [2], [3], [1, 2], [2, 3], [1, 3], [1, 2, 3]]

Given [1, 2], return
[
  [],
  [1],
  [2],
  [1,2]
]

Given [1, 2, 2, 2] return
[
  [],
  [1],
  [2],
  [2],
  [2],
  [1, 2],
  [2, 2],
  [2, 2],
  [2, 2]
  [1, 2],
  [1, 2],
  [1, 2, 2],
  [2, 2, 2],
  [1, 2, 2],
  [1, 2, 2]
  [1, 2, 2, 2]
]

## Break It Down ##

Seeing that we can have multiple numbers of the same type, we would need to figure out a way to distinguish equal numbers as distinct. We can do this by identifying numbers by their index.

We can try to do this recursively first starting with the whole list and appending it to the sets. Afterwards, we can iterate through the list and at every step we run the main method recursively adding the current list to the set of subsets. The key that we will be running original list minus the value in the current index.

So at a high level, it would look like this:

whole = [1, 2, 3]
subsets = []

First iteration:

add whole to subset :
[[1, 2, 3]]

Iterate through whole:
  remove ith value from list and recurse

This would add
[2, 3], [1, 3], and [1, 2] to subsets

subsets [[1, 2, 3], [2, 3], [1, 3], [1, 2]]

Iterate through [2, 3], [1, 3] and [1, 2]

Each one would add the following to subset:

[2, 3] -> [2], [3]
[1, 3] -> [1], [3]
[1, 2] -> [1], [2]

To avoid duplicates, we can use a set.

We can also avoid duplicates by doing the same approach but in a bottom-up manner. So instead of starting with the whole list, start with an output list that contains the empty subset.

From there we will create a helper function called findSubsets that will take the current subset and the rest of the list.

The findSubsets method will iterate through the nums list. At each step, it will add the subset of the current list (with the addition of the current value we are at in the index) and also recursively run findSubsets again with the newly updated subset and the rest of the list minus the one just added to the subset. 
