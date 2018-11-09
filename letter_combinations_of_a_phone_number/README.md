# 17. Letter Combinations of a Phone Number #

**Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.**

## Clarifying Questions ##

1. Does order of combinations matter?
2. Will the string contain more than 2 digits?

Order of combination does not matter and we will assume that the string can contain more than 2 digits.

## First Approach ##

So the first thing I want to do is map every digit from 2 to 9 to the three letters they are assigned on a phone. We can do this by creating a dict.

After we completely mapped the numbers to strings, we can start producing all possible letter combinations. To find all unique permutations, we are going to need a set to save our letter combinations. We will do this by creating a permutations function.

The permutations function will take the digits we will use, the string generated so far, the set containing the letter combos, and number-letters map. At every step, we will see if we reached the end of the string. If we have not, then we slice off the first letter of the digits and grab its letter representation. We also get the remaining digits not used and set it to the rest variable. Now we will iterate through the letter representation. At every letter, we will recursively run our permutation function, adding the current letter to the string generated so far and using rest as the digits left over.

This method will create all unique letter combinations. 
