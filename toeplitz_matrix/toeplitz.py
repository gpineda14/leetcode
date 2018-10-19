def isToeplitzMatrix(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(0, col - 1):
        r = 0
        c = i
        curr = matrix[r][c]

        while r < row and c < col:
            if matrix[r][c] != curr:
                return False
            r += 1
            c += 1

    for i in range(0, row - 1):
        r = i
        c = 0
        curr = matrix[r][c]

        while r < row and c < col:
            if matrix[r][c] != curr:
                return False
            r += 1
            c += 1

    return True
