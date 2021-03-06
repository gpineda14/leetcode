# 345. Reverse Vowels of a String #

**Write a function that takes a string as input and reverse only the vowels of a string.**

## Clarifying Questions ##

1. What is considered a vowel in this context?

2. Will the string contain any punctuation or spaces?

Let's assume that there will be no punctuation but there will be spaces.

## First Approach ##

We will create a stack to keep track of all vowels. Every vowel we find, we will replace with a carrot ^ and also push it to the stack. We will also split the string into an so we can loop through it.

We are going to do two passes. The first pass we will iterate through the array, adding vowels to the stack and changing the vowels to ^ in the array.

In the second pass, we will pop off the vowel from the stack and replace every ^ with it.

Finally we will join the array and return it.

## Refactor ##

We can also approach this problem by creating two pointers, one at the start of the string and one at the end.

We will increment and/or decrement the start and/or end pointer based on the following conditions:

1. if a[start] and a[end] are not vowels:
  - increment start
  - decrement end
2. if a[start] is not a vowel:
  - increment start
3. if a[end] is not a vowel:
  - decrement end
4. if a[start] and a[end] are vowels:
  - swap values
  - increment start
  - decrement start 
