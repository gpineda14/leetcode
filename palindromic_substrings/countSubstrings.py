def countSubstrings(s):
    count = 0
    arr = list(s)
    sz = len(arr)
    for i in range(sz):
        for j in range(i + 1, sz + 1):
            if isPalindrome(arr[i:j]):
                count += 1

def isPalindrome(arr):
    return arr == arr[::-1]
