def lengthOfLastWord(s):
    if len(s) == 0:
        return 0

    letterIndex = 0
    end = len(s) - 1
    while end >= 0:
        if s[end].isalpha():
            letterIndex = end
            break
        end -= 1

    spaceIndex = letterIndex
    while spaceIndex >= 0:
        if s[spaceIndex] == " ":
            break
        spaceIndex -= 1

    return letterIndex - spaceIndex
