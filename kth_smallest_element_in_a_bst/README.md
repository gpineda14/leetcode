# 230. Kth Smallest Element in a BST #

**Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.**

## Understanding the problem ##

We are asked to find the kth smallest value in the tree. We can do this by sorting the tree is ascending order and returning the kth value. We can take advantage of the structure of the binary search tree by doing an inorder traversal, appending every value to a list. We are given the list as input and an integer k. Our output should be an integer.

## Concrete Examples ##

Given [3, 1, 4, null, 2], k = 1
return 1

Given [5, 3, 6, 2, 4, null, null, 1], k = 3
return 3

Given [5, 4, 3, 2, 1], k = 2
return 2

Given [8], k = 1
return 8

## Break it down ##

1. create a numbers variable to hold all values in bst
2. do an inorder traversal on the tree, appending value to the list
3. return the (k - 1)th value in the numbers array.
