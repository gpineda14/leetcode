def findAnagrams(s, p):
    if s == p:
        return [0]

    indices = []
    hashmap = {}
    size = len(p)

    for i in range(0, len(s) - size + 1):
        index = 1
        sub = s[index:index+size]
        if (isAnagram(sub, p)):
            indices.append(index)

    return indices

def isAnagram(str, p):
    hashmap = {}

    for char in p:
        if char in hashmap:
            hashmap[char] += 1
        else:
            hashmap[char] = 1

    for char in str:
        if char in hashmap:
            hashmap[char] -= 1
            if hashmap[char] < 0:
                return False
            else:
                return False

    return True 
