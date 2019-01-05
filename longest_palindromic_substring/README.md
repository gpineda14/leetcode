# 5. Longest Palindromic Substring #

**Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.**

## Understanding the problem ##

Given a string, we want to see what is the longest palindrome present in the string and return that particular substring. We can fix the string to a starting position and ending position and periodically check if the string is a palindrome. If it is and it is larger than our current max size, then we keep track of the indices and update our current max size. After we exhaust our search, we return the string with the indices we stored.

## Concrete Examples ##

given "babad",
return "bab" or "aba"

given "cbbd",
return "bb"

given "aaaaaaaa"
return "aaaaaaaa"

given "abababa"
return "abababa"

given "abca"
return "a" | "b" | "c"

## Break it down ##

1. create a sz variable to keep track of largest palindrome
2. create a list that will keep track of indices of largest palindrome
3. Create an outer loop that will be fixed as the starting position
4. Create an inner loop that will be fixed as the ending position
5. Within the inner loop check if substring[start:end] is a palindrome
  - If palindrome, check if larger than sz and if it is, update indices to start, end
6. return largest palindrome
