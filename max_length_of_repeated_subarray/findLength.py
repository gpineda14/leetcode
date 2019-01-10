def findLength(A, B):
    blen = len(B)
    alen = len(A)
    indices = collections.defaultdict(list)
    global_max = 0
    for idx, elem in enumerate(A):
        indices[elem].append(idx)

    for i, elem in enumerate(B):
        if indices[elem]:
            for idx in indices[elem]:
                local_max = 0
                bPtr = i
                aPtr = idx
                while bPtr < blen and aPtr < alen and B[bPtr] == A[aPtr]:
                    local_max += 1
                    bPtr += 1
                    aPtr += 1
                if local_max > global_max:
                    global_max = local_max

    return global_max
