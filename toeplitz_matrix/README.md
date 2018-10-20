# 766. Toeplitz Matrix #

***A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.***

## Clarifying Questions ##

1. Are we allowed to use extra memory?
2. Will the matrix rows and columns differ? i.e are we dealing only square matrices?

## First Approach ##

So we want to validate a matrix and see if every diagonal contains the same element. So the obvious way to solve would be to go through every diagonal in the matrix and ensure all values in a diagonal are equal.

So given matrix :

[
  [1, 2, 3, 4],
  [5, 1, 2, 3],
  [9, 5, 1, 2]
]

We can begin with the first diagonal beginning at matrix[i][j] where i = 0, j = 0. From there, we can increment both i and j by 1 to continue along the diagonal.

To ensure we get all the diagonal, I am going to going to fix the row and go along all the diagonals that begin there

This will get us the half the diagonals and to get the rest I would do the same, except fix the col and go down the rows and check those diagonals.

After that, we successfully check all the diagonals
