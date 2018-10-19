# 617. Merge Two Binary Trees #

***Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.***

## Clarifying Questions ##

1. Do we have to merge the binary tree into an existing binary tree or can we merge them to a new binary tree?

***I'm going to merge them to an existing binary tree for this exercise***

## First Approach ##

So I'll first check if either t1 or t2 is None.

If t1 is None, then we return t2 and we are done. If t2 is None, then we return t1 and we are done.

If both t1 and t2 are valid TreeNodes, then we increment the value of t1 by t2.value. Afterwards we go down through the tree recursively by setting t1.left to mergeTrees(t1.left, t2.left) and t1.right to mergeTrees(t1.right, t2.right)
