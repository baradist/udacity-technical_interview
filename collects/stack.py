import collects.linked_list


class Stack:
    def __init__(self):
        self.ll = collects.linked_list.LinkedList()

    def push(self, value):
        self.ll.add_first(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.ll.remove_first()

    def peek(self):
        if self.is_empty():
            return None
        return self.ll.get(0)

    def is_empty(self):
        return self.ll.is_empty()
