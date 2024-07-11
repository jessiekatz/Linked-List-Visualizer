class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.numItems = 0

    def add_node(self, val):
        newNode = Node(val)
        if (not self.head):
            self.head = newNode
        else:
            curr = self.head
            while (curr.next):
                curr = curr.next
            curr.next = newNode

    def remove_node(self, val):
        if self.head is None:
            return
        if self.head.val == val:
            self.head = self.head.next
            self.numItems -= 1
            return
        current = self.head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
                self.numItems -= 1
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    def print_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.val)
            current = current.next
        return result
