# 58. Length of Last Word #

***Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.***

## Clarifying Questions ##

1. Would a single word with no spaces be considered a last word?

2. What would an empty string be considered?

## First Approach ##

Okay I want to iterate through the string until I reach the first letter from the end. If I don't reach any, then we return 0 because there is no final word. Once I find the first letter from the end. I then iterate from that letter and search until we find the a space. We keep track of the index the space is located. Then we return firstletter - spacelocation.
