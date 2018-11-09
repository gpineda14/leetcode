def findAndReplacePattern(words, pattern):
    matches = []
    for i in range(0, len(words)):
        if isOneToOne(words[i], pattern):
            matches.append(words[i])
    return matches

def isOneToOne(word, pattern):
    m1 = {}
    m2 = {}
    for w, p in zip(word, pattern):
        if w not in m1:
            m1[w] = p
        if p not in m2:
            m2[p] = w
        if (m1[w], m2[p]) != (p, w):
            return False
        return True 
