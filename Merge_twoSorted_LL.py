class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

    def insert(self, newData):
        newNode = Node(newData)
        if self.head is None:
            self.head = newNode
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = newNode


def mergeSortedLists(head1, head2):
    temp = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = mergeSortedLists(head1.next, head2)

    else:
        temp = head2
        temp.next = mergeSortedLists(head1, head2.next)

    # return the temp list.
    return temp


# Create 2 lists
head1 = LinkedList()
head2 = LinkedList()

head1.insert(1)
head1.insert(2)
head1.insert(4)
head1.insert(6)
head1.insert(9)

head2.insert(3)
head2.insert(4)
head2.insert(7)
head2.insert(8)

head1.head = mergeSortedLists(head1.head, head2.head)
head1.printList()

