# 191. Number of 1 Bits #

**Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).**

## Clarifying Questions ##

No clarifying questions, this one seems pretty straightforward

## First Approach ##

Okay so we need to create a count variable that will keep track of all 1 bits in the number n.

One way to do this is by clearing the least significant. To do this will loop while n is still is greater than 0. At every iteration, we set n = n & (n -1). This will clear the least significant bit. Every time we clear the least significant bit, we increment the count by 1.

After the iteration is complete, count should be equal to the number of 1 bits in n. 
