# 566. Reshape the Matrix #

***In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.***

## Clarifying Questions ##

1. Can we assume that the new matrix will be completely filled?

***The new matrix must be filled completely so if the new reshaped matrix has empty cells, then return the original matrix***

## First Approach ##

So the first thing I want to do is make sure that I can create a valid matrix. We can do this by checking if the rows * columns of original matrix is equal to the new rows * col. If they are we can continue, else return original matrix

Next we create a new list with r many lists.

Next we fill every new row with c elements. We can do this by iterating through the original matrix. We also create a pointer to indicate the current row we are in our new matrix. Once the length of new matrix is equal to c, then we increment the row to begin the process again until we reach the new of the original matrix.
