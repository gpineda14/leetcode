def swapPairs(head):
    return recSwap(head)

def recSwap(head):
    if head is None:
        return head
    if head.next is None:
        return head

    curr = head
    upNext = head.next
    rest = upNext.next
    upNext.next = curr
    upNext.next.next = recSwap(rest)
    return upNext
