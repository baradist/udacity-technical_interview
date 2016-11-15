
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList(object):
    first = None
    last = None
    _size = 0

    def __init__(self, value=None):
        if not value == None:
            self.add_first(value)

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_first(self, value):
        f = self.first
        new_element = Element(value)
        new_element.next = f
        self.first = new_element
        if not f:
            self.last = new_element
        else:
            f.previous = new_element
        self._size += 1

    def add_last(self, value):
        l = self.last
        new_element = Element(value)
        new_element.previous = l
        self.last = new_element
        if not l:
            self.first = new_element
        else:
            l.next = new_element
        self._size += 1

    def get(self, position):
        return self.__get_element(position).value

    def insert_before(self, value, index):
        after = self.__get_element(index)
        new_element = Element(value)
        if after == self.first:
            self.first = new_element
            new_element.next = after
            after.previous = new_element
        else:
            before = after.previous
            new_element.previous = before
            before.next = new_element
            new_element.next = after
            after.previous = new_element

        self._size += 1

    def remove(self, index):
        removable = self.__get_element(index)
        if self.first == removable and self.last == removable:
            self.first = None
            self.last = None
        elif self.first == removable:
            removable.next.previous = None
            self.first = removable.next
        elif self.last == removable:
            removable.previous.next = None
            self.last = removable.previous
        else:
            removable.previous.next = removable.next
            removable.next.previous = removable.previous
        self._size -= 1

    def __get_element(self, index):
        if index < 0 or index >= self._size:
            raise Exception("IndexOutOfBoundsException, position =", index, ", size =", self._size)
        if index == self._size:
            return self.last
        counter = 0
        current = self.first
        while current and counter <= index:
            if counter == index:
                return current
            current = current.next
            counter += 1
        return None
