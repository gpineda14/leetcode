def kthSmallest(matrix, k):
    heap = []
    size = len(matrix)
    for i in range(size):
        for j in range(len(matrix[i])):
            heapq.heappush(heap, matrix[i][j])

    curr = None
    while k > 0:
        curr = heapq.heappop(heap)
        k -= 1
    return curr
