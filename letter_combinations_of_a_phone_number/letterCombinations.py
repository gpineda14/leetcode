def letterCombinations(digits):
    if digits == "":
        return []

    letters = string.ascii_lowercase
    start = 0
    end = 3
    combos = {}
    total = set()
    for i in range(2, 10):
        if i == 7 or i == 9:
            end += 1
        combos[i] = letters[start:end]
        start = end
        end += 3

    permutations(digits, "", total, combos)
    return list(total)

def permutations(digits, so_far, total, combos):
    if not digits:
        total.add(so_far)
        return
    first = digits[0]
    rest = digits[1:]
    letters = combos[int(first)]
    for letter in letters:
        permutations(rest, so_far + letter, total, combos)
