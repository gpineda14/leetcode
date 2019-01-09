# Path Sum III #

**You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.**

## Understand the problem ##

So we are asked to find the number of paths equate to the sum in a binary tree. There is a new constraint, which is that the path does not need to start at a root or end at a leaf. They do, however, have to be consecutive. We are given a binary tree and an integer as input. We are to output the number of ways we can add up the nodes to equal sum.

## Concrete Examples ##

Given [10, 5, -3, 3, 2, null, 11, 3, -2, null, 1], 8
return 3

Given [5, 10, 1], 1
return 1

Given [10, 9, 8, 3, 4], 7
return 0

Given [8, 4, 4, 4, 3], 8
return 2

## Break it down ##

We can recursively search through the tree and add up the values until it equates to the sum. If values becomes greater than sum, the we can set it back to 0 and keep searching down the tree if there are any children.

1. create a helper function that will find all paths that equal to sum
  - takes tree, sum, and array as input
  - if tree is none, return 0
  - add value in current node to array
  - create a count variable to keep track of how many times we get the sum
  - create a curr variable to keep track of current sum
  - iterate through the array in reverse to replicate root to path, but also get paths in between
    - increment curr by n
    - if curr == sum, add 1 to count
  - return found + helper(left) + helper(right)
2. return result of helper function
