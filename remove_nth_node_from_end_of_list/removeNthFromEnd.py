def removeNthFromEnd(head, n):
    size = 0
    ls = head
    slow = head
    fast = head.next

    while ls:
        size += 1
        ls = ls.next

    if size == n:
        return head.next

    target = size - n

    while target > 1 and fast:
        slow = slow.next
        fast = fast.next
        target -= 1

    slow.next = fast.next
    return head
    
