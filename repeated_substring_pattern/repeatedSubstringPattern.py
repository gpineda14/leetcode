def repeatedSubstringPattern(s):
    max_sub = len(s) // 2 + 1
    for i in range(1, max_sub):
        curr = s[:i]
        sub = s[:i]
        while len(curr) <= len(s):
            curr += sub
            if curr == s:
                return True
    return False

def repeatedSubstringPatternFaster(s):
    length = len(s)
    max_sub = length // 2 + 1
    if length <= 1:
        return False

    for i in range(1, max_sub):
        if length % i == 0:
            str = s[i:] + s[0:i]
            if str == s:
                return True
    return False
