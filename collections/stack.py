class Node:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class Stack:
    def __init__(self, value=None):
        self.first = Node(value)

