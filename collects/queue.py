import collects.linked_list


class Queue:
    def __init__(self):
        self.ll = collects.linked_list.LinkedList()

    def add(self, value):
        self.ll.add_last(value)

    def poll(self):
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

    def size(self):
        return self.ll.size()