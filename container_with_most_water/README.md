# 11. Container With Most Water #

**Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.**

## Understand the Problem ##

We are given an array of values where each value indicates a height. We can get the width by index of array. So we want to find the two values at i and j that give us the largest area. We then want to output that area.

We know that the area is of length n and n is at least 2. We also know that the values will not be sorted in the array. We can use two pointers to find the height of the array. The issue will be find the conditions to use when moving pointers forward and to also figuring out where to put the pointers.

## Concrete Examples ##

Given [1, 8, 6, 2, 5, 4,8,3,7]
return 49

Given [1, 1, 2, 2, 4, 1]
return 4

Given [1, 4, 6, 3, 6, 2]
return 12

## Break it down ##

1. create a max_area variable to keep track of max size
2. Do an outer for loop, fixing value at i as first endpoint
3. Do a inner loop from i + 1 to end of array
  - find area given two endpoints and set max_area to the max of max_area and curr_area
4. return max_area

This method will pass 45/50 test cases on leetcode until it the time limit exceeds

## Refactor ##

We can try solving this problem using two pointers. We can set one pointer at the beginning and the other at the end. The condition we are going to use to keep the pointers moving is if the new area is larger than the current max area. We check at both endpoints and keep advancing while left endpoint is less then right endpoint

1. find max_area which is left - area * min(arr[left], arr[right])
2. set max_area to max of max_area and area given current left and right
3. if height[left] < height[right], increment left
4. else decrement right
5. return max_area
