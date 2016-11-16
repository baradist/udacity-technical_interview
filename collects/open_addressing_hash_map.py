class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.l = [0 for i in range(0, capacity)]
        self._size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._find_index(key)
        if not self.l[index]:
            if self._size == self.capacity: # todo
                raise Exception("Nowhere to put, map is full, size and capacity =", self.capacity)
            self._size += 1
        self.l[index] = Node(key, value)

    def get(self, key):
        return self.l[self._find_index(key)].value

    def _find_index(self, key):
        index = self._hash(key)

        while self.l[index] and self.l[index].key != key:
            index += 1
            if index == self.capacity:
                index = 0
        return index
