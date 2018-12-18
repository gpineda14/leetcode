# 451. Sort Characters By Frequency #

**Given a string, sort it in decreasing order based on the frequency of characters.**

## Understanding the problem ##

We are given a string and we are to figure out a way to reorganize it such that the most frequently occurring string comes first and so on.

The input a string and because we know it is immutable, we should split it into an array. Some things to consider is whether uppercase and lowercase letters are considered equal. We should also check if only alphabetic characters will be in the string. Will numeric values be considered invalid?

The output we are expected is a string. Its string should be modified according to the frequency of its characters.

## Concrete Examples ##

Given "abc", return
"abc" || "bac" || "acb"

Given "aaabcc", return
"acb"

Given "AAaBb", return
"AAaBb" || "AABba" || "AAbBa" || "AAbAB"

Given "aaaccc", return
"aaaccc" || "cccaaa"

Given "abababab", return
"aaaabbbb" || "bbbbaaaa"

## Break it down ##

We want to modify the string so I'm going to need to split it into a list so I can manipulate the structure.

Afterwards, we need to keep track of all its characters and frequency. We can use a dictionary to keep track of the character frequencies.

Finally, we have to figure out a way sort the array by frequency. We can do a sort method and add in a lambda into our sort method.

Finally we can join the array to create a string and return it.

## Looking Back ##

Looking back, I see that it would be better to store the values in a min-heap. We can negate the values and add the lowest to the front of the string. This would give us a better runtime because we are most focused on repeated values instead of sorting. 
