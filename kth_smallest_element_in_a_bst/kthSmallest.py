def kthSmallest(root, k):
    nums = []
    inorder(nums, root)
    return nums[k - 1]

def inorder(nums, tree):
    if tree:
        inorder(nums, tree.left)
        nums.append(nums.val)
        inorder(nums, tree.right)
        
