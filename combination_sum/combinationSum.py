def combinationSum(candidates, target):
    combos = []
    findCombos(candidates, target, combos, [], 0)
    return combos

def findCombos(candidates, target, combos, curr, index):
    if target < 0:
        return
    if target == 0:
        combos.append(curr)
        return
    for i in range(index, len(candidates)):
        curr.append(candidates[i])
        findCombos(candidates, target - candidates[i], combos, curr, i)
        curr.pop()
