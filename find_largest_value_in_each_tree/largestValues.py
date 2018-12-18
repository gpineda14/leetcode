def largestValues(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [root.val]

    max_values = []
    levels = [root]

    while levels:
        temp = []
        max_values.append(max[node.val for node in levels])
        for level in levels:
            if level.left:
                temp.append(level.left)
            if level.right:
                temp.append(level.right)

        levels = temp

    return max_values
