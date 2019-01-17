def reverseVowelsOptimized(s):
    vowels = 'aeiouAEIOU'
    start = 0
    end = len(s) - 1
    letters = list(s)
    while start < end:
        if letters[start] not in vowels and letter[end] not in vowels:
            start += 1
            end -= 1
        elif letters[start] not in vowels:
            start += 1
        elif letters[end] not in vowels:
            end -= 1
        else:
            letters[start], letters[end] = letters[end], letters[start]
            start += 1
            end -= 1
    return ''.join(letters)
