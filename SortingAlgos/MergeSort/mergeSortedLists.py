'''
l1 = 1 -> 3 -> 5
l2 = 2 -> 4 -> 6

out = 1->2->3->4->5->6
'''


class listNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def mergeSortedLists(l1: listNode,l2: listNode) -> listNode:
    mergedHead = l1 if l1.val < l2.val else l2
    cursor = listNode(-1)
    cursor.next = mergedHead


    # Merge until  one of the lists depleted
    while l1 and l2:
        if l1.val < l2.val:
            cursor.next = l1
            l1 = l1.next
        else:
            cursor.next = l2
            l2 = l2.next
        cursor = cursor.next

    remaining = l1 if l1 else l2

    while remaining:
        cursor.next = remaining
        remaining = remaining.next
        cursor = cursor.next


    return mergedHead

def printList(head):
    while head:
        print(head.val)
        head = head.next

def main():
    l1 = listNode(5)
    l1.next = listNode(33)
    l1.next.next = listNode(122)
    printList(l1)
    print()

    l2 = listNode(6)
    l2.next = listNode(433)
    l2.next.next = listNode(2222)
    printList(l2)
    print()

    mergedHead = mergeSortedLists(l1,l2)
    printList(mergedHead)
    print()


if __name__ == "__main__":
    main()




