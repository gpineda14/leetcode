def productExceptSelf(nums):
    size = len(nums)
    output = []
    prev = 1

    for i in range(size):
        output.append(prev)
        prev *= nums[i]

    prev = 1
    for j in range(size - 1, -1, -1):
        output[j] *= prev
        prev *= nums[j]

    return output
