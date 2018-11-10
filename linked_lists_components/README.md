# 817. Linked Lists Components #

**We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear consecutively in the linked list.**

## Clarifying Questions ##

1. Is the ordering of G relevant or it just random?
2. Will there only be unique values in the linked list? Do we have to take into account duplicates?

## First Approach ##

Some variables we will need are: a count variable to keep track of all connected components and two pointer variable for our linked list (ptr1 and ptr2), and a curr variable that will keep track of the size of the current component.

We will be doing 2 passes. The first pass we will search through the linked list and look for values that are not in G. If a value is not in G, then we will replace the value with an X. The second pass will then count up the size of every component using the curr variable. If the value in the linked list is not X, then we increment curr. Once we reach an X, if the curr value is greater than 0, then we will increment the count variable by 1. If curr is 0, we do not increment count.

## Second Approach ##

We can also use all the same variables, but instead do it in one pass. While we are iterating through the array, we are checking if the current node value is in G. If it is, then we are incrementing our curr value. If the current node value is not in G, then if curr is greater than 0, we have found a component and increment count by 1 and reset curr to 0. 
