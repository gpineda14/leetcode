# 19. Remove Nth Node From End of List #

**Given a linked list, remove the n-th node from the end of list and return its head.**

## Clarifying Questions ##

1. Will n always be less than the length of the linked list
2. If n is equal to 1, should the last number be removed

## First Approach ##

So we will solve this problem by find the length of the linked list and subtracting n from the length of the linked list. The new value tells us how many iterations we will need to make to reach the node that is nth from the end of the list.

We will now do a second pass on the linked list. We will be using two pointers. One will start at the beginning of the list and the other one will start at the subsequent node. While k > 0, we will iterate through the linked list. At every iteration, we will update the pointers to the next values. After the iterations, the first pointer should be pointing at the value before the node that is to be deleted. The second pointer should be pointer at the node that needs to be deleted. So we will set the next value of the first pointer to the next value of the second pointer. After that, we should have the linked list with the intended node deleted.  
