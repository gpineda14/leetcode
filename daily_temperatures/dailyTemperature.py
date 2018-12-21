def dailyTemperatures(T):
    waiting_times = []
    sz = len(T)
    for i in range(sz):
        curr = T[i]
        wait = 0
        steps = 0
        for j in range(i + 1, sz):
            steps += 1
            if curr < T[j]:
                wait += steps
                break
        waiting_times.append(wait)
    return waiting_times
