def threeSum(nums):
    combos = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        while l < r:
            if nums[i] + nums[l] + nums[r] < 0:
                l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                if left > (i + 1) and nums[l] == nums[l - 1]:
                    l += 1
                    continue
                combos.append([nums[i], nums[l], nums[r]])
                l += 1
    return combos
