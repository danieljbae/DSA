class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def printList(self, head):
        out = ""
        while head:
            out += str(head.val) + " -> "
            head = head.next
        print(out + "None")

    def buildList(self, ls):
        assert len(ls) >= 1, print("List must contain values")
        dummy = ListNode(-1)
        dummy.next = cursor = ListNode(val=ls[0])
        for val in ls:
            cursor.next = ListNode(val)
            cursor = cursor.next
        return dummy.next

    def mergeSort(self, head):
        if not head or not head.next:
            return head
        # Recursively Divide
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None
        left, right = self.mergeSort(head), self.mergeSort(mid)

        # merge until one list is depleted
        mergedHead = dummy = ListNode(-1)
        while left and right:
            if left.val < right.val:
                mergedHead.next = left
                left = left.next
            else:
                mergedHead.next = right
                right = right.next
            mergedHead = mergedHead.next

        # Determine which one is depleted
        remaining = left if left else right
        mergedHead.next = remaining
        return dummy.next


def main():
    ls = LinkedList()
    ls.head = ls.buildList([5, 6, 4, 3, 1])
    ls.printList(ls.head)
    ls.sortedHead = ls.mergeSort(ls.head)
    ls.printList(ls.sortedHead)


if __name__ == '__main__':
    main()


# def mergeSort(ls):
#     if len(ls) > 1:
#         # Recursively Divide
#         mid = len(ls) // 2
#         left = ls[:mid]
#         right = ls[mid:]
#         mergeSort(left)  # Recursively Sort
#         mergeSort(right)

#         # merge until one list is depleted
#         l = r = mergedIdx = 0
#         while l < len(left) and r < len(right):
#             if left[l] < right[r]:
#                 ls[mergedIdx] = left[l]
#                 l += 1
#             else:
#                 ls[mergedIdx] = right[r]
#                 r += 1
#             mergedIdx += 1

#         # Determine which one is depleted
#         remaining, remainIdx = (left, l) if l < len(left) else (right, r)
#         while remainIdx < len(remaining):
#             ls[mergedIdx] = remaining[remainIdx]
#             remainIdx += 1
#             mergedIdx += 1


# ls = [7, 4, 8, 3, 1, 4, 6, 2, 5]
# print(ls)
# mergeSort(ls)
# print(ls)
