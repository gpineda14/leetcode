def numComponents(head, G):
    curr = 0
    count = 0
    ptr1 = head

    while ptr1:
        if ptr1.val not in G:
            ptr1.val = 'x'
        ptr1 = ptr1.next

    ptr2 = head

    while ptr2:
        if ptr2.val != 'x':
            curr += 1
        else:
            if curr > 0:
                count += 1
                curr = 0
        ptr2 = ptr2.next

    if curr > 0:
        count += 1
    return count

def numComponentsFaster(head, G):
    curr = 0
    count = 0
    ptr1 = head
    gSet = set(G)

    while ptr1:
        if ptr1.val not in gSet:
            if curr > 0:
                count += 1
                curr = 0
        else:
            curr += 1
        ptr1 = ptr1.next

    if curr > 0:
        count += 1
    return count 
