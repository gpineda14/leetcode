# 783. Minimum Distance Between BST Nodes #

**Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.**

## Clarifying Questions ##

1. Should we return 0 if the tree is empty?
2. Can we assume the BST will always be valid?

## First Approach ##

We can do this by using a stack. We create a variable called min_diff and set it to infinity. We will also create a prev_node variable that will keep track of the last visited node. We will also create a stack variable that will be used to facilitate an in-order traversal. As we perform the inorder traversal, we will find the difference between prev_node and the current node and if it is less than min_diff, then we set min_dff to abs(prev_node - curr node). 
