# 287. Find the Duplicate Number #

**Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

1. You must not modify the array (assume the array is read only).
2. You must use only constant, O(1) extra space.
3. Your runtime complexity should be less than O(n2).
4. There is only one duplicate number in the array, but it could be repeated more than once.**

## Understand the problem ##

We are given an array of size n + 1 and we want to return the duplicate value. We know the array will only contain numbers from 1 to n.

We cannot modify the array and we can only use constant space. We should be returning the duplicate value. It should be pretty trivial to find the duplicate value, but we have to do it without using extra space or modifying the array. This means we can't use any sorting solutions.

We have to figure out a way to find a duplicate without changing the array or sorting.

## Concrete Examples ##

given [1, 2, 3, 3, 4]
return 3

given [5, 6, 2, 3, 1, 5, 5]
return 5

given [1,3, 4, 2, 2]
return 2

given [3, 1, 3, 4, 2]
return 3

given [6, 1, 2, 2, 5, 7, 2, 3]
return 2

given [6, 5, 4, 2, 2, 1]
return 2

given [2, 3, 1, 2]
return 2

## Break it down ##

This problem can be reduced to cycle detection

1. Create a slow and fast pointer
2. Find the intersection of the two runners with the help of the pointers
3. Create two more pointers to find the entrance or duplicate value in the array
4. Find duplicate with the help of the two runners.
5. Return the duplicate 
