# 189. Rotate Array #

**Given an array, rotate the array to the right by k steps, where k is non-negative.**

## Clarifying Questions ##

1. What should the function return when k is equal to 0? What if k is greater than the length of nums.

## First Approach ##

We want to rotate the array to the right by k steps. So to do that, we have to reorient the start of the array. To do this, we're going to subtract the length the array by k. This, in turn, will give us the starting place of our rotated array. Now we need to run two iterations. The first one from our new starting point until the end of the array. The second iteration, we start at 0 and end at length of array - k. The final array will be the rotated array.

This solution works, but it requires us to use O(n) space for the new array.

## Second Approach ##
