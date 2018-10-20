def largestGroupPositions(S):
    groups = []
    i = 0
    while i < len(S):
        index = i
        curr = S[index]
        end = index + 1
        while end < len(S) and S[end] == curr:
            end += 1
        if end - index >= 3:
            groups.append([index, end - 1])
        i = end
    return groups
