# 129. Sum Root to Leaf Numbers #

**Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.**

## Understanding the problem ##

Given a tree, I want to find all the numbers that each path forms. After I find the numbers, I want to sum them all up and return the sum.

The input given is going to be a tree of values. The tree can possibly be empty, so in that case, we should return 0. The trees should have integers as numbers, however and characters will be considered invalid input. The output should be an integer that is the sum of all numbers created by the paths of the tree. By paths, I mean the collection of nodes it takes to reach a leaf from the root node. A leaf node is a node with no children.

We can find the path numbers by searching through the binary tree so we have all the information we need to find the sum.

## Concrete Examples ##

Given (4) (4 5) ((1 3), ())
return 441 + 443 + 45 = 929

Given (1) (1) ((1 2))
return 111 + 112 + 11 = 123

Given (3) (4 5) ((4 5) (4 5))
return 344 + 345 + 354 + 355 = 1398

## Break it down ##

1.  Create a sum variable and a list to hold all the path numbers
2. search through the list and find all the path numbers
  a. if tree is not null, use it in the recursive function
  b. given a string, we will append the current value in node to the string
  c. If both left side and right side of tree is None, then we reached a leaf node and need to append the string to the list
  c. If there is still a left side or a right side, then we recursively run the function again on that part of the tree.
3. add up all the path numbers in the list and return its sum
