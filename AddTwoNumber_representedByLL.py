class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    node = ListNode()
    current = node
    carry = 0

    while l1 or l2 or carry:
        sum_val = carry

        if l1:
            sum_val += l1.val
            l1 = l1.next
        if l2:
            sum_val += l2.val
            l2 = l2.next

        carry = sum_val // 10
        current.next = ListNode(sum_val % 10)
        current = current.next

    return node.next

# Example usage
# Create the first linked list: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create the second linked list: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Add the linked lists
result = addTwoNumbers(l1, l2)

# Print the resulting linked list: 7 -> 0 -> 8
current = result
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")
