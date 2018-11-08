def rotate(nums, k):
    # Method with Extra Space
    start = len(nums) - k
    result = []
    for i in range(start, len(nums)):
        result.append(nums[i])
    for j in range(0, start):
        result.append(nums[j])
    return result
