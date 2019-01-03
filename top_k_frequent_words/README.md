# 692. Top K Frequent Words #

**Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.**

## Understanding the problem ##

The problem asking us to return the top k most occurring strings in a list. The input will be a list of strings and an integer k that has to be between 1 and the length of the list. The output will be a list of size k that will contain the top k frequent words in the original list.

We can get the input from the input by counting the number of occurrences of every string in the input list. We can do this with a collections counter. From there we can sort those occurrence values by highest to lowest. We can then extract the first k values and search for the corresponding key in the collections counter.

We can also use a heap to find the top k values, which might be a better solution.

## Concrete Examples ##

Given ['i', 'love', 'leetcode', 'i', 'love', 'coding'], 2
return ['i', 'love']

Given [a, a, a, a, b, c, c, c, d], 4
return [a, b, c, d]

Given [a, b], 1
return [a]

Given [x, y, x, a, z, a, a, z, d], 3
return [a, x, z]

## Break it down ##

1. create key-value pair that has string as key and occurrence as value, we can use collections.counter
2. we sort the values by value of k (occurrence)
  - use a tuple
  - add key,values to heap
3. pop the top k values and corresponding keys
  - use list comprehension
