def isValid(s):
    stack = []
    size = len(s)
    for i in range(0, size):
        curr = s[i]
        if curr == '[' or curr == '{' or curr == '(':
            stack.append(curr)
        else:
            popped = None
            if len(stack) > 0:
                popped = stack.pop()
            else:
                return False

            if curr == '}' and popped != '{':
                return False
            elif curr == ')' and popped != '(':
                return False
            elif curr == ']' and popped != '[':
                return False

    if len(stack) > 0:
        return False
    else:
        return True 
