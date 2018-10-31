def maxDepth(root):
    if root is None:
        return 0
    if root.children == []:
        return 1
    else:
        height = [maxDepth(c) for c in root.children]
        return max(height) + 1
