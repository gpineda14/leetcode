# 532. K-diff Pairs in an Array #

**Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.**

## Clarifying Questions ##

1. Will all values in the array be positive?
2. Are (1, 3) and (3, 1) considered unique?

We will not consider (1, 3) and (3, 1) as unique characters.

## First Approach ##

So we want to find all pairs in the array where their absolute difference equals k. So I will create a nested look. The outer loop will fix the first value of the pair on i. The outer loop will the set the first value to the values from i to len(a) - 1 of the array. The inner loop will set the second value of the pair to the i + 1 value in the array. We will also create a count variable to keep track of the kdiff pairs. We also want to keep track of all pairs, so we need to create a pairs variable that makes a dict of all pairs whose diff are equal to k.

Every time the absolute difference of the i and i + 1 value equals to k, we increment the count variable. Finally we return the count variable.

This results worse, but it leads to an suboptimal solution.

## Second Approach

This time will we create a dict that will contain all values of the array as a key. The value will be the number of times the key appears in the array. We will still need the count variable to keep track of unique pairs.

For example: [1, 2, 3, 1] would translate to: {1: 2, 2: 1, 3: 1}

Afterwards, we will loop through the keys in the dict. If k > 0, then every time that k + key is in the diff, we increment count by 1. This is true because k = key1 - key2, where key1 and key2 are keys in the dict. So if k + key1 is in the dict, then we have a unique pair. If k == 0, then we just need to see that the key in dict has more than 1 value that is equal to key. If that is the case, then we increment count by 1

Finally we return count.
