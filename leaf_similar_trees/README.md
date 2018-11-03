# 872. Leaf-Similar Trees #

**Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.**

## Clarifying Questions ##

Don't have any, it seems pretty straightforward

## First Approach ##

Okay so we want to see if the two trees, root1 and root2, are leaf-similar. To do so, we will create a array that holds the leaf value sequence for every tree. We can do this by running a DFS on every tree. From there we can compare the two arrays to ensure they are equal.
