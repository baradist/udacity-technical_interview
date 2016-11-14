
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList(object):
    size = 0

    def __init__(self, value=None):
        if not (value == None):
            self.add_first(value)

    def add_first(self, value):
        f = self.first
        new_element = Element(value)
        new_element.next = f
        self.first = new_element
        if not f:
            self.last = new_element
        else:
            f.previous = new_element
        self.size += 1;

    def add_last(self, value):
        l = self.last
        new_element = Element(value)
        new_element.previous = l
        self.last = new_element
        if not l:
            self.first = new_element
        else:
            l.next = new_element
        self.size += 1;

    def get(self, position):
        element = self.__get_element(position)
        if element:
            return element.value
        return None

    def __get_element(self, position):
        if position < 0:
            return None
        counter = 0
        current = self.first.next
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self, value, position):
        if (position < 0 or position >= self.size):
            raise Exception("IndexOutOfBoundsException, position =", position, ", size =", self.size)
        new_element = Element(value)
        after = self.__get_element(position)
        if (after == self.first):
            new_element.next = after
            self.first = new_element
        else:
            before = after.previous
            new_element.previous = before
            before.next = new_element

        if (after == self.last):
            new_element.previous = after
            after = self.last
        else:
            after = after.next
        new_element.previous = before
        before.next = new_element
        new_element.next
        self.size += 1;

    def remove(self, index):
        pass

    def find(self, value):
        """Find the first node with a given value. Return the index"""
        current = self.first.next
        previous_node = None
        while current.value != value and current.next:
            previous_node = current
            current = current.next
        if (current):
            if (previous_node):
                previous_node.next = current.next
            else:
                self.first.next = current.next
            if current == self.last:
                self.last = previous_node
        self.size -= 1;

    def reverse(self):
        newList = LinkedList()


# Test cases

# Start setting up a LinkedList
ll = LinkedList(0)

# Should print 0 now
print ll.get(0)

ll.add_first(1)
ll.add_first(2)

# Test get_position
# Should print 2
print ll.get(2)

# Test insert
ll.insert(3, 2)

print "size:", ll.size

# Should print 3 now
print ll.get(2)

# Test delete
ll.delete(1)
# Should print 0 now
print ll.get(0)
# Should print 3 now
print ll.get(1)
# Should print 2 now
print ll.get(2)

print "size:", ll.size
