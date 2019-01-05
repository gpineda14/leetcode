def longestPalindrome(s):
    sz = 0
    indices = []
    lg = len(s)
    for i in range(lg):
        for j in range(i + 1, lg + 1):
            if isPalindrome(s[i:j]):
                if j - i > sz:
                    sz = j - 1
                    indices = [i, j]
    return s[indices[0]:indices[1]]

def longestPalindromeDP(s):
    sz = len(s)
    sub = [[False] * sz for _ in sz]
    if sz == 0:
        return ""

    max_len = 1
    start = 0

    for i in range(sz):
        sub[i][i] = True

    for i in range(sz - 2 + 1):
        if s[i] == s[i + 1]:
            sub[i][i + 1] = True
            max_len = 2
            start = i

    for lens in range(3, sz + 1):
        for i in range(0, sz - lens + 1):
             j = i + lens - 1
             if sub[i+1][j-1] and s[i] == s[j]:
                 sub[i][j] = True
                 if (len > max_len):
                     max_len = lens
                     start = i

    return s[start:start+max_len]

def isPalindrome(s):
    return s == s[::-1]
