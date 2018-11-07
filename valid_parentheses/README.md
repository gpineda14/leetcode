# 20. Valid Parentheses #

**Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.**

## Clarifying Questions ##

1. Will the string only contain parentheses?

For this case, we will strings will only contain, parentheses-type characters

## First Approach ##

This is a common stack-based problem. We will iterate through the string, setting the current string as curr. All opening parentheses such as '(', '{', '[' will be pushed onto our stack variable. For closing parentheses, we will pop the last character added to the stack and set it to our popped value. Afterwards we have to consider three cases:

1. popped = '{' and curr != '}'
2. popped = '[' and curr != ']'
3. popped = '(' and curr != ')'

All three cases should return False because in those scenarios, we have invalid parenthesis.

After we finish iterating through the string, we then have to check if the stack is empty. If the stack is empty, then the string contained a set of valid parentheses and return true. If it is not empty, then we have a set of invalid parenthesis and we must return false.
