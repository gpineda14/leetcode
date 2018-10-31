def leafSimilar(root1, root2):
    a1 = dfs(root1, [])
    a2 = dfs(root2, [])

    if len(a1) != len(a2):
        return False
    else:
        index = 0
        size = len(a1)
        while index < size:
            if a1[index] != a2[index]:
                return False
            index += 1
        return False

def dfs(tree, arr):
    if tree is None:
        return
    if tree.left is None and tree.right is None:
        arr.append(tree.val)

    dfs(tree.left, arr)
    dfs(tree.right, arr)
    return arr
