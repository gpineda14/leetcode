class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mergeTwoBinaryTrees(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.left = mergeTwoBinaryTrees(t1.left, t2.left)
    t1.right = mergeTwoBinaryTrees(t1.right, t2.right)
    return t1
