class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

    def delete_recursive(self, head, key):
        if not head:
            return None

        if head.data == key:
            return head.next

        head.next = self.delete_recursive(head.next, key)

         
        return head
    
    # Create a linked list and add some nodes
llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

llist.head.next = second
second.next = third
third.next = fourth

print("Original list:")
llist.print_list()

# Delete node with value 3
llist.head = llist.delete_recursive(llist.head, 3)

print("List after deleting 3:")
llist.print_list()

# Delete node with value 1 (head node)
llist.head = llist.delete_recursive(llist.head, 1)

print("List after deleting 1 (head node):")
llist.print_list()

# Delete node with value 4
llist.head = llist.delete_recursive(llist.head, 4)

print("List after deleting 4:")
llist.print_list()
