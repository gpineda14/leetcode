def minSubArrayLen(s, nums):
    n = len(nums)
    min_len = sys.maxsize
    left = 0
    sum = 0
    for i in range(n):
        sum += nums[i]
        while sum >= s:
            min_len = min(min_len, i + 1 - left)
            sum -= nums[left]
            left += 1
    return min_len if min_len != sys.maxsize else 0
