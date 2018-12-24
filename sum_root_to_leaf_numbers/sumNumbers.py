def sumNumbers(root):
    output = 0
    path_numbers = []
    num = ""
    findPathNum(num, root, path_numbers)
    return output + sum([int(i) for i in path_numbers])

def findPathNum(st, tree, tree):
    if tree is None:
        return
    st += str(tree.val)
    if not (tree.left or tree.right):
        arr.append(st)
    if tree.left:
        findPathNum(st, tree.left, arr)
    if tree.right:
        findPathNum(st, tree.right, arr)
