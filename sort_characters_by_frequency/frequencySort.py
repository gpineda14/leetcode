import heapq
def frequencySort(s):
    heap = []
    frequencyMap = collections.Counter(s)
    for key in frequencyMap:
        heapq.heappush(heap, -(frequencyMap[key], key))

    res = ""
    while heap:
        pair = heapq.heappop(heap)
        multiplier = -pair[0]
        char = pair[1]
        res += char * multiplier

    return res
