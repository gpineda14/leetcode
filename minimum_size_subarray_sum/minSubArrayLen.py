def minSubArrayLen(s, nums):
    if sum(nums) < s:
        return 0
    sz = len(nums)
    global_min = sz
    for i in range(sz):
        start = nums[i]
        count = 1
        if start >= s:
            global_min = min(global_min, count)
        for j in range(i + 1, sz):
            start += nums[j]
            count += 1
            if start >= s:
                global_min = min(global_min, count)
    return global_min
