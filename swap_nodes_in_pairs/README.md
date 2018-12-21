# 24. Swap Nodes in Pairs #

**Given a linked list, swap every two adjacent nodes and return its head.

Your algorithm should use only constant extra space.

You may not modify the values in the list's nodes, only nodes itself may be changed.**

## Understanding the problem ##

Given a linked list, we want to swap every two adjacent nodes and return the solution.

We have to be sure to use constant space and we cannot change the values in the nodes. We can, however, change the nodes themselves.

This looks like a problem that can make use of pointers. One pointer can keep track of its current value. Another pointer can keep track of its next value.

We can also make this a recursive function. We swap the next and curr value and then append the remainder to the recursive function.

## Concrete Examples ##

Given 1 -> 2, return 2 -> 1

Given 2 -> 1 -> 3, return 1 ->2 -> 3

Given 4 -> 3 -> 2 -> 1, return 3 -> 4 -> 1 -> 2

Given 1 -> 2 -> 3 -> 4 -> 5, return 2 -> 1 -> 4 -> 3 -> 5

Given 1, return 1

Given 5 -> 5 -> 5 -> 5 -> 1, return 5 -> 5 -> 5 -> 5 -> 1

## Break it down ##

We are going to do a recursive function

Base Case: if linked list does not have a next value, return the linked list

Inductive Step:

1. create a curr and upNext variable
2. set curr to linked list and upNext to head.next
3. set upNext.next to curr
4. set upNext.next.next to the recursive function
5. return upNext
