def findDuplicates(nums):
    duplicates = []
    values = {}
    size = len(nums)
    for i in range(0, size):
        if nums[i] in values:
            values[nums[i]] += 1
        else:
            values[nums[i]] = 1

        if values[nums[i]] > 1:
            duplicates.append(nums[i])

    return duplicates

def findDuplicates2(nums):
    duplicates = []
    nums.sort()
    for i in range(0, len(nums)):
        if nums[i] == nums[i + 1]:
            duplicates.append(nums[i])
    return duplicates
