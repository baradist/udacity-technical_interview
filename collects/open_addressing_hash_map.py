class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.l = [0 for i in range(0, capacity)] # todo
        self._size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        if self._size == self.capacity:
            raise Exception("Nowhere to put, map is full, size and capacity =", self.capacity)
        index = self._find_index(key)
        if not self.l[index]:
            self._size += 1
        self.l[index] = Node(key, value)

    def put_all(self, map):
        if self._size + map.size() >= self.capacity:
            raise Exception("Nowhere to put, map is full, size and capacity =", self.capacity, "(trying to add", map.size())
        for i in range(0, map.capacity):
            if map.l[i]:
                self.put(map.l[i].key, map.l[i].value)

    def get(self, key):
        return self._get(key).value

    def _get(self, key):
        return self.l[self._find_index(key)]

    def size(self):
        return self._size

    def _find_index(self, key):
        index = self._hash(key)

        while self.l[index] and self.l[index].key != key:
            index += 1
            if index == self.capacity:
                index = 0
        return index
