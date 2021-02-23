class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class List:
    def __init__(self, head=None):
        self.head = ListNode()

    def buildList(self, head, array):
        if not array:
            return None
        self.head = cursor = ListNode(val=array[0], next=None)
        for i in range(1, len(array)):
            cursor.next = ListNode(val=array[i], next=None)
            cursor = cursor.next

        return self.head


def mergeKlists(lists):
    if not lists:
        return lists
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2
    left, right = mergeKlists(lists[:mid]), mergeKlists(lists[mid:])
    return merge(left, right)


def merge(left, right):
    dummy = merged = ListNode(-1)
    while left and right:
        if left.val < right.val:
            merged.next = left
            left = left.next
        else:
            merged.next = right
            right = right.next
        merged = merged.next
    merged.next = left or right
    return dummy.next


def main():
    lists = [[3, 4, 5, 7], [3, 3, 8, 9], [1, 12]]
    linkedLists = []
    for ls in lists:
        currList = List()
        currHead = currList.buildList(currList, ls)
        linkedLists.append(currHead)

    mergedLists = mergeKlists(linkedLists)
    while mergedLists:
        print(mergedLists.val)
        mergedLists = mergedLists.next


if __name__ == "__main__":
    main()
