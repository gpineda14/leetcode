# 890. Find and Replace Pattern #

**You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.**

## First Approach ##

So we want to sift through the array and see which one has a one-to-one mapping with the pattern variable. We will create a function called isOneToOne that will return true if the current element in array is a one to one mapping the the pattern. If the element returns true, we will add it to our array matches.

Now we have to create the isOneToOne function. It will accept two strings, one is a string in the array (curr) and the other is the pattern. We will use a hash map to help us. We will use the characters in curr as values and map them to corresponding characters in the pattern. We will also do the reverse, setting characters in pattern as key and characters in curr as values. After we complete the mapping on both sides. We will do this using the zip function on the word and pattern. We then will iterate through both of them, setting current character as w and p. We have two maps set up, m1 and m2. If w is not in m1, we then set m1[w] = p. If p is not in m2, we then set m2[p] = w. Afterwards, we check if m1[w], m2[p] equal p, w because m1[w] should map to p and m2[p] should map to w.
