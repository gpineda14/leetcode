def matrixReshape(nums, r, c):
    row = len(nums)
    col = len(nums[0])

    if row * col != r * c:
        return nums

    matrix = [[] for x in range(0, r)]
    curr_row = 0

    for i in range(0, col):
        for j in range(0, row):
            matrix[curr_row].append(nums[i][j])
            if len(matrix[curr_row]) == c:
                curr_row += 1

    return matrix
