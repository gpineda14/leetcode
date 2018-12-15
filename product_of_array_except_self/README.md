# 238. Product of Array Except Self #

**Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Please solve it without division and in O(n).**

## Initial Thoughts/Questions ##

So if we can't use division, then we can try iterate through the list len(nums) times. Every time we will create a new value that multiplies against every number in nums except i. We will add this new value to our output list.

## First Approach ##

We will create an index variable i that will keep track of which number not to include in the product.

At every iteration we will multiply up the values of the numbers in num. If we reach the index i, we will make sure not to multiply it against the product. After we are done with the multiplication, we will append the new value to our output list.

This works, however the time complexity of the algorithm is O(N^2) so we need to find a way to do this faster.

## Second Approach ##

If we want to use multiplication, we can do one pass to find the product of all values in nums. Afterwards, we can do a second pass in all the numbers in nums, dividing our max product by the current number in nums.

This will give us a O(n) solution, but involves us using multiplication and can become more complicated when values in the nums list are 0.

## Third Approach ##

The final method we use involves using the output as a prefix product. We set the first value of output to prev, which will 1. After that we will multiply prev by nums[i].

This will give use the product of all the values of nums from 0 to i - 1 at position i. Resetting the prev value to 1.

We will now iterate starting at the end of the list. We will set the value at j equal to output[j] * prev. The value at j will be product of all values before j in the original list and the prev variable will keep track of the product of the values after j.

This solution gives us a linear time complexity without having to use division. 
