def searchInsert(nums, target):
    larger = 0
    found = False
    size = len(nums)

    for i in range(0, size):
        if nums[i] == target:
            return i
        else:
            if nums[i] > target and not found:
                larger = i
                found = True

    if not found:
        larger = size

    return larger
