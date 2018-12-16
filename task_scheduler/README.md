# 621. Task Scheduler #

**Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.**

## Understanding the problem ##

So given a list of task, we have to find the number of intervals it would take to complete the tasks if only 1 task can be done per interval. We also have to satisfy the cooling interval condition where two same tasks have to have be n intervals apart.

The given input is a list of characters where different characters represent different tasks and an integer n that represents the number of intervals we have to wait until we can do a previous task. We know that there will be 26 different possible tasks because there are 26 letters in the alphabet and that n can be between 0 and 100 inclusively. The list itself can also have up to 10,000 tasks.

We are expected to return an integer that represents the least number of intervals required for the CPU to finish all the tasks and adhere to its cooling interval.

I believe we would need to create a list that will hold all the intervals. We would also need to create a data structure that will keep track of all the various types of tasks.

## Concrete Examples ##

a. Given ls = [a] and n = 10, return 1

b. Given ls = [a, a] and n = 1, return 3
[a, idle, a]

c. Given ls = [a, b, a, b] and n = 0, return 4
[a, b, a, b]

d. Given ls = [a, b, b, b, b, b] and n = 10, return 45
[b, a, idle * 9, b, idle * 1-,
 b, idle * 10, b, idle * 10,
 b, idle * 10]

 e. Given ls = [a, a, a, a, a, b, b, b, b, c, c, c] and n = 5, return 25

 f. Given ls = [a, a, a, b, b, b] and n = 2
 [a, b, idle, a, b, idle, a, b]
 return 8

 g. Given ls = [a, b, c, a, b, c, a, b, c] and n = 2
return 9

## Breaking it down ##

Looking at our concrete examples (in particular c and d), We see that we can mathematically find the least number of intervals required by first finding the most frequently occurring task and set its frequency to mostFrequent. After that we can find the least number of intervals required by the following equation:

((mostFrequent - 1) * n) + mostFrequent

This equation works because given the requirement of satisfying the cooling interval, we know that just the most frequently occurring task is going need n intervals of space, so that gives us mostFrequent * n. However we don't need the interval of space after the last value, so that gives us (mostFrequent - 1) * n. We also have to keep track of the task itself, which gives us the addition of mostFrequent.

So the steps go as

1. Find frequency of all similar tasks
2. Find the most frequent task and set it to mostFrequent
3. Return the result of the equation above
