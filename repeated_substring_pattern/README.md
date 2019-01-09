# 459. Repeated Substring Pattern #

**Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.**

## Understanding the problem ##

We are given a string and we are to inspect if the string can be reproduce by multiple instances of a substring within the string. We know that the string will only consists of lowercase english letters. The output will be a boolean indicating whether we can concatenate a number of substrings to produce the input string.

We are going to have to take a number of substrings from the string, so we'll need a variable hold the current substring. Other than that, we can try to iterate through the list, produce a substring and keep adding the to substring until its equal or greater than the input string. At every addition, we can check the substring to the original string.

## Concrete Examples ##

Given "aaa", return True
Given "abc", return False
Given "abba", return False
Given "aaaaa", return True
Given "abcdeabcde", return True
Given "a", return False
Given "aa", return True

## Break it down ##

1. find the length of input string and halve it and set it to max_sub
2. loop through string from 1 to max_sub
  - set curr to input_string[:i]
  - set sub = input_string[:i]
  - nested loop, loop until curr >= s
    - add sub to curr
    - check if curr is equal to input_string
      - if equal return true 
3. return false

## Time and Space Complexity ##

Time Complexity: O(n^2)
Space Complexity: O(n)
