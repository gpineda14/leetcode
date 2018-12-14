# 938. Range Sum of BST #

**Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.**

## Initial Thoughts/Questions ##

So the first thing that comes to mind is doing an inorder depth first search to have the values in sorted order and then locating the left value and the right value. Once we locate those values, we will use a variable to sum up the values from left to right.

This approach assumes all trees given as input are binary search trees that obey the BST property.

## First Approach ##

So doing an inorder depth firs search is pretty trivial. I will do the search, adding the values into an array. I do not want to search through the array for the left and right value so what I will also do is create an x, y, and index variable. The index value will keep track of the index. As we add values to the array, we will check if they match the left or right value and if it does we will set x or y to index.

With a sorted array and the position of x and y. We will create a sum variable and iterate through the sorted values from the index x to y, adding them to the sum variable.

## Second Approach ##

It seemed a bit unnecessary to have an x and y variable to keep track of index. What we could do instead is a traditional inorder traversal and check if every value is between L and R. If it is, we will increment it to our global sum variable.
