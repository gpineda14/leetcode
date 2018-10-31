# 559. Maximum Depth of N-ary Tree #

***Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.***

## Clarifying Questions ##

1. What would be the depth of a tree with just a head?

## First Approach ##

We can solve this problem using a DFS search. We can do this recursively. If the tree is None, then the height of the tree is 0. If the tree does not have any children, then return 1. If the tree does have children, then we can recursively run the maxDepth function for every child of the tree. Finally we return the max of the children plus 1. This will result in the max depth of the N-ary tree. 
