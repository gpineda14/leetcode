# 35. Search Insert Position #

**Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.**

## Clarifying Questions ##

1. If there is duplicates, which index should we return?
2. Can we guarantee that the input will have the target value?

## First Approach ##

Well its pretty trivial searching for the target value, we just have to loop through the array until we find the target value and then return its index.

However, if the target value is not present in the array then we need to return the index where the target value would have been. To do this, we need to keep track of the first value that is larger than the target value because the location of that one will be where the target value should have been. 
