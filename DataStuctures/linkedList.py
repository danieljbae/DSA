class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self,head):
        cursor = head
        while cursor:
            print(cursor.val)
            cursor = cursor.next

def main():
    l = LinkedList()
    l.head = Node(0)
    l.head.next = Node(1)
    l.head.next.next = Node(2)

    l.printList(l.head)

if __name__ == '__main__':
    main()

# Python command line w/ Classes:

# option 1) Use variables in Main
    # import linkedList as l
    # l.main() -> 1,2,3 ...

# option 2) Unit testing functions
    # import linkedList as l
    # head = l.Node(99)
    # head.next = l.Node(98)
    # l.printList(head) -> 99, 98, ...
