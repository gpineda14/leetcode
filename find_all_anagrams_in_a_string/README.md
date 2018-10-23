# 438. Find All Anagrams in a String #

***Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.***

## Clarifying Question ##

1. Will there be overlapping anagrams in the string?

2. Will the string contain uppercase and lowercase letters?

3. Does order of output matter?

## First Approach ##

First we want to get the length of the string p. We also want to create a list of indices that will hold all relevant indices. We also want to create a hash map of all the values in p. Then we want to iterate through the whole list. At every iteration, we want to get substring from i to i + len(p). We then will use a helper function called isAnagram and use the substring and the hash map as input. The isAnagram will then loop through the substring and check off all of its values that are in the hash map. If the value is not in the hashmap, then we return false and move to the next substring. If the anagram is a substring, then we return true and then add the index to the indices list. After we iterate through the whole list, we return the the indices list.

This solutions works but it leads to an inefficient solution. When I tried it on LeetCode, it was able to pas 34/36 of the test cases until it passed the time limit.

## Second Approach ##

Okay lets keep the hashmap of p, the indices list.
