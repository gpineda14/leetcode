def rangeSumBST(root, L, R):
    def inorder(tree, lt, rt):
        if tree:
            if lt <= tree.val <= rt:
                ans += tree.val
            if lt < tree.val:
                inorder(tree.left, lt, rt)
            if tree.val < rt:
                inorder(tree.right, lt, rt)

    ans = 0
    inorder(root, L, R)
    return ans 
