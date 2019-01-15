# 3. Longest Substring Without Repeating Characters #

**Given a string, find the length of the longest substring without repeating characters.**

## Understand the problem ##

We are given a string and we are supposed to find the length of the largest substring that contains no duplicates within it. The output will be a integer indicating size of substring. The input will be a string that may or may not contain duplicates. The input may also be an empty string.

We can iterate through the list and by scanning through it we can find the length of the longest substring with unique values.

We will need a variable to keep track of the max size of substring, a temp variable to build out the substring.

## Concrete Examples ##

given "abcabcbb"
return 3

given "bbbbb"
return 1

given "pwwkkew"
return 3

given "abcdefa"
return 6

given "tdeed"
return 3

given "pzke"
return 4

given "pizooki"
return 4

## Break it down ##

1. create variable to keep track of max_len
2. create a hash map to keep track of how many times an element occurs
3. create two pointers, i and j
4. we are going to keep iterating while i < len(s)
5. we are know going move the j pointer inside
  - if map[arr[j]] > 1, move i pointer forward, compare max_lens, set j = i + 1.
6. return max length
