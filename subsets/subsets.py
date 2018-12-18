def subsets(nums):
    output = [[]]
    findSubsets([], nums, output)
    return output

def findSubsets(curr, nums, output):
    for index, value in enumerate(nums):
        output.append(curr + [value])
        findSubsets(curr + [value], nums[index + 1:], output)
