# 187. Repeated DNA Sequences #

**All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.**

## Initial Thoughts/Questions ##

So we want to return the set of 10 letter sequences that occur more than once in the DNA molecules.

The first thing I want to do is to identify all the possible 10 letter sequences. This is pretty simple to do because all 10 letter sequences are consecutive.

After we identify all the ten letter sequences, we want search through the string again and if a particular 10 letter sequence from the set occurs more than 1, then we want to save it and add it to our list of sequences that occurred more than once.

## First Approach ##

So I first want to find all possible 10-letter sequences. To do this, I will create a dict that will have a sequence as key with a value set to 0. 

So to find the 10-letter sequences is pretty simple. We will use two pointers, start and end. We will set start to 0 and end to 9. We will iterate through the string, capturing the substring from index start to end. At each step, we will increment start and end by 1.

Afterwards, we will iterate through the string again, grabbing the substring from start to end and increment every substring by 1. If a particular substring has a value greater than 1, we add it to our list of repeated_dna.

We then return the repeated_dna list.
