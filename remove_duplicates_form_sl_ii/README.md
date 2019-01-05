# 82. Remove Duplicates from Sorted List II #

**Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.**

## Understanding the problem ##

Given a linked list, we want to return the linked list with all values that occur more than once removed. So we want to not only remove duplicates but also the value itself. This means we want only values that occur only once in the list.

We can try to create a counters map to keep track of all values. Afterwards, we can iterate through the original list and transfer the values that occur once in a new list. We can check against the counters map to see how many times a value is present.

## Concrete Examples ##

given 1->2->3->3->4->4->5
return 1->2->5

given 1->1->1->1->1
return None

given 1->1->1->2->3
return 2->3

given 5->5->6->7->8
return 6->7->8

## Break it down ##

1. Make a collections counter to keep track of all values in linked list
2. create a new list
3. Iterate through list and count values
4. Iterate again, adding to the new list values that only occur once in the original list
5. return new list
