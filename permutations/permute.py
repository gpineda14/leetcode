def permute(nums):
    perm = []
    sz = len(nums)

    makePermutations(perm, [], nums, sz)
    return perm

def makePermutations(perm, currPerm, waitingList, whole):
    if len(currPerm) == whole:
        perm.append(currPerm)
        return
    for index, val in enumerate(waitingList):
        makePermutations(perm, currPerm + [val], waitingList[:index] + waitingList[index + 1:], whole)
