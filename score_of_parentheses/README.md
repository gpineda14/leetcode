# Score of Parentheses #

***Given a balanced parentheses string S, compute the score of the string based on the following rule:

-() has score 1
-AB has score A + B, where A and B are balanced parentheses strings.
-(A) has score 2 * A, where A is a balanced parentheses string.***

## Clarifying Questions ##

1. Will there be empty strings? If so, what would their scores be?

## First Approach ##

When I think of balanced parentheses, I usually associate those with stack-based problems. So first I would like to create a stack variable initialized with a 0. Whenever a "(" pops up, I will append a 0 to the end of the stack. If its a ")", I will pop off the last value in the stack and set it to val. Then I will set the last value of stack to the max of val * 2 and 1. The answer will then be the last value in the stack so we return that to get the answer. 
