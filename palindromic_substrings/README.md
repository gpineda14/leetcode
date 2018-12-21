# 647. Palindromic Substrings #

**Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.**

## Understanding the problem ##

So what the question is asking us is, given a string, how many palindromes are in the string?

We see that the input is going to be a list and we want to output a integer denoting the number of palindromes. We know a palindrome is a string that is equal to its reversed counterpart.

The problem does make some important decisions that give us some insights into the solution. For example, it says substrings with different start or end indices are counted as different substrings. It also says that strings of single characters are considered palindromes. This means we are probably going to have to check for palindromicity at every index in the string and have to build up strings at new indices. This also means we do not have to worry about duplicate values since different indices will be considered different substrings.

## Concrete Examples ##

Given "a", return 1

Given "abab", return 6

Given "aaabbbccc", return 18

Given "baab", return 6

## Break it down ##

1. Create a count variable and split the string into an array.
2. We want to split the array into various subarrays and test each string for palindromicity
  a. Create a nested for loop, where the inner loop will indicate start of subarray and outer loop will indicate end of subarray
  b. at every step, we will test for palindromicity
  c. if it is a palindrome, we increment count by 1
3. return count


## Look back and refactor ##

This solution works but the time complexity is O(n^3) where n is the length of the string. The outer for loop has a time complexity of O(n) and each loop in that has O(n) iterations as well, giving us O(n^2). At each iteration of the inner loop, we check for palindomicity, which is an O(n) operation as well.
