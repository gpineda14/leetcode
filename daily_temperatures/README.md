# 739. Daily Temperatures #

**Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].**

## Understanding the problem ##

Given a list temperatures, we want to see how many days will it take until we get warmer temperature. So given temperature on the ith day, we want to see how many days it will take until we reach the a warmer temperature. Once we reach a warmer temperature, we want to add the time it takes into a list that keeps track of the wait times.

The input is going to be a list of temperatures, which can duplicate temperatures. The output is a list of waiting times. We can find the waiting by searching through the daily temperature list. The output will be a list of integers.

We want to have list to keep track of waiting times. We will also try to iterate through the list, fix the current value at i. Within the iteration we will have a second iteration from i to the end of the list. We will look through until we find the next largest value.

## Concrete Examples ##

given [40, 50, 60, 34],
return [1, 1, 0, 0]

given [31, 32, 100, 56, 33, 30]
return [1, 1, 0, 0, 0, 0]

given [41, 44, 40, 39, 32, 49, 37]
return [1, 4, 3, 2, 1, 0, 0]

given [31]
return [0]

given [35, 35]
return [0, 0]

## Break it down ##

1. create a waiting_times list to keep track of wait times
2. Iterate through the temperatures
3. At every iteration, set curr to temp[i] and wait to 0 and steps to 0
4. We will have a nested for loop go from i to len(temperature)
5. At every iteration we will increment steps and if a value is greateer than temp[i], then add steps to wait and break
6. Add wait to waiting_times
7. return waiting_times

## Look back and refactor ##

This solution works, but it gives us a O(n^2) time complexity and make us do a lot of repeated work.  
