def deleteDuplicates(head):
    counter = collections.Counter()
    ptr1 = head
    ptr2 = head
    newHead = ListNode(0)
    nPtr = newHead

    while ptr1:
        counter[ptr1.val] += 1
        ptr1 = ptr1.next

    while ptr2:
        if counter[ptr2.val] == 1:
            nPtr.next = ListNode(ptr2.val)
            nPtr = nPtr.next
        ptr2 = ptr2.next

    return newHead.next
