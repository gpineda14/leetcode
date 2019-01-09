def pathSum(root, sum):
    return pathSumHelper(root, sum, [])

def pathSumHelper(root, sum, visited):
    if not root:
        return 0
    visited += [root.val]
    count = 0
    curr = 0
    for n in visited[::-1]:
        curr += n
        if curr == sum:
            count += 1
    return count + pathSumHelper(root.left, sum, visited) + pathSumHelper(root.right, sum, visited)
