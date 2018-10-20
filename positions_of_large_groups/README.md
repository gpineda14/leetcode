# 830. Positions of Large Groups #

***In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.***

## Clarifying Questions ##

1. Is the array sorted?

2. Are duplicate groups allowed?

I'm going to assume array is not sorted and contents of the groups do not matter, so long as they are all the same and greater than or equal to 3

## First Approach ##

So I would like to iterate through the string. I would then keep track of the current index and set up a new variable called end. The end variable will increment so long as its equal to array[index]. Once the value at end no longer is equal to the value at index. We then subtract end - index, if its larger than or equal to 3, then we add it to the array and we also set index to end. We continue to do this while index is less than length of string
