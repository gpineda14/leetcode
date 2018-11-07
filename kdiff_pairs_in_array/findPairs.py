def findPairs(nums, k):
    # Bruteforce Method
    # pairs = {}
    # count = 0
    # for i in range(0, len(nums) - 1):
    #     for j in range(i + 1, len(nums)):
    #         diff = abs(nums[i] - nums[j])
    #         pair = (nums[i], nums[j])
    #         if k == diff and pair not in pairs:
    #             pairs[nums[i], nums[j]] = True
    #             pairs[nums[j], nums[i]] = True
    #             count += 1
    # return count

    kdiff = {}
    count = 0
    for i in range(0, len(nums)):
        if nums[i] in kdiff:
            kdiff[nums[i]] += 1
        else:
            kdiff[nums[i]] = 1

    for key in kdiff.keys():
        if k > 0 and key + k in kdiff or k == 0 and kdiff[key] > 1:
            count += 1

    return count
