# 442. Find All Duplicates in an Array #

**Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?**

## Clarifying Questions ##

1. Can I do this with extra space?
2. Will there be more than 2 elements of the same value?

## First Approach ##

This looks like a good candidate for a hash map. We can iterate through the list, keeping a count of all values in the array. As we keep track of the count, we will also check if the current element has reached a count greater than or equal to 2. If it is, then we will add it to my new duplicates array. At the end, we should return the duplicates array.

## Second Approach ##

The second does not require extra space, but does take longer than the first approach. We first sort the array. After sorting the array, we then iterate through the list. Next we compare the adjacent values, i and i + 1. If the elements in index i and i + 1 are equal, then we have a duplicate value and add it to the duplicates array. After the iteration completes, we return the duplicates array.

## Third Approach ##

Like the other two previous methods, we will create a duplicates array that will contain our duplicate elements. Now we will iterate through the elements in the array. We now will use every element n as the index by decrementing the element by 1. Every element at index n - 1 will be negated. So if any number at n - 1 is negative, then we know that is a duplicate value because we previously negated the value. After iterating through the values, we return the duplicates array.
