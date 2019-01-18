def search(nums, target):
    n = len(nums)
    if n == 0:
        return - 1
    if n == 1:
        return 0 if nums[0] == target else -1
    rotate_index = find_rotate_index(0, n - 1)

    if nums[rotate_index] == target:
        return rotate_index
    if rotate_index == 0:
        return b_search(0, n - 1)
    if target < nums[0]:
        return b_search(rotate_index, n - 1)
    return b_search(0, rotate_index)

def b_search(left, right):
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        else:
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

def find_rotate_index(left, right):
    if nums[left] < nums[right]:
        return 0

    while left <= right:
        pivot = (right + left) // 2
        if nums[pivot] > nums[pivot + 1]:
            return pivot + 1
        else:
            if nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1
