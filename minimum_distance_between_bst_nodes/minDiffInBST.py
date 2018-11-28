def minDiffInBST(root):
    diff = float('inf')
    prev_node = None
    stack = []
    node = root

    while stack or node is not None:
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if prev_node and node.val - prev_node.val < diff:
                diff = node.val - prev_node.val
            prev_node = node
            node = node.right
    return diff
