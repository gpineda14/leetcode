def arrayNesting(nums):
    sz = len(nums)
    values = [False] * sz
    ans = 0
    for i in range(sz):
        if not values[i]:
            start = nums[nums[i]]
            count = 1
            while (start != nums[i]):
                start = nums[start]
                count += 1
                values[start] = True
            ans = max(ans, count)
    return ans 
