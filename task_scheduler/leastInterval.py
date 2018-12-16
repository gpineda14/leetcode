def leastInterval(tasks, n):
    if n == 0:
        return len(tasks)

    frequent = collections.Counter(tasks)
    mostFrequent = max(frequent.values())
    max_frequent_count = 0
    for value in frequent.values():
        if value == mostFrequent:
            max_frequent_count += 1

    return ((mostFrequent - 1) * n) + mostFrequent + (max_frequent_count - 1)
