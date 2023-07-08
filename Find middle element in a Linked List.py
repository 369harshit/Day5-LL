class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMiddle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Move slow pointer one step further to get the second middle node
    if fast:
        slow = slow.next

    # Retrieve the values of the second middle node and subsequent nodes
    result = []
    while slow:
        result.append(slow.val)
        slow = slow.next

    return result


# Helper function to create a linked list from a list of values
def createLinkedList(values):
    node = ListNode(0)
    current = node

    for val in values:
        current.next = ListNode(val)
        current = current.next

    return node


# Example usage
values = [1, 2, 3, 4, 5, 6]
linked_list = createLinkedList(values)

second_middle_values = findMiddle(linked_list)

print("Result:", second_middle_values)
