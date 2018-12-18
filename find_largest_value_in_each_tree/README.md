# 515. Find Largest Value in Each Tree #

**You need to find the largest value in each row of a binary tree.**

## Understanding the problem ##

So given a tree, we need to find the largest value in each level. The output then should be a list of numbers that represent the largest values in each level. We can obtain the solution if we can find a way to augment the values of the tree at every level and extract the max value.

The input will be a tree. If the tree is empty, then we should return an empty list. If the tree has only a root value, we should return a list with the root value only. If the tree has children, we need extract its left and right child and their respective values. If a node does not have any children, we do not want to add a null value to the tree.

We will need a list to hold the nodes at each level. We will also need a list to hold all the max values in each level.

## Concrete Examples ##

Given (1) (2 3) ((4 5) (6 7))
return [1, 3, 7]

Given (6)
return [6]

Given ()
return []

Given (6) (4 6) ((8) (1 2))
return [6, 6, 8]

## Break it down ##

1. Create a list to hold max values and another list to hold values at every level. We want to add the root node to the levels list.
2. Iterate through the tree, one level at a time
3.  Extract max value from the levels list and add to max value
4. Overwrite levels list with children of current nodes in the list 
5. Return list of max values
