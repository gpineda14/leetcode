def maxSlidingWindow(nums, k):
    i = 0
    j = k
    max_window = []
    while i < len(nums) and j < len(nums) + 1:
        max_window.append(max(nums[i:j]))
        i += 1
        j += 1
    return max_window 
