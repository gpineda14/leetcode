def reverseVowels(s):
    stack = []
    vowels = 'aeiou'
    arr = list(s)
    size = len(arr)
    for i in range(0, size):
        if arr[i] in vowels:
            stack.append(arr[i])
            arr[i] = '^'

    for i in range(0, size):
        if arr[i] == '^':
            arr[i] == stack.pop()

    return "".join(arr)
