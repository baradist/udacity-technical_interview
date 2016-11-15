import collects.linked_list


class Stack:
    def __init__(self):
        ll = collects.linked_list.LinkedList()

    def push(self, value):
        self.ll.add_first(value)

    def pop(self):
        if self.is_empty():
            return None
        value = self.ll.get(0)
        self.ll.remove(0)
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.get(0)

    def is_empty(self):
        return self.ll.is_empty()