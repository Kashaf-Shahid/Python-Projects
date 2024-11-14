class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.head:
            return None
        popped_node = self.head
        self.head = self.head.next
        return popped_node.data

    def peek(self):
        if not self.head:
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
