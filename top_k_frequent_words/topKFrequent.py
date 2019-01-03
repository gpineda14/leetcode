def topKFrequent(words, k):
    occurrences = collections.Counter(words)
    heap = [(-freq, word) for word, freq in occurrences.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]
