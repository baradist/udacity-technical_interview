import collects.open_addressing_hash_map


class HashSet:
    def __init__(self, capacity):
        self.capacity = capacity
        self.l = collects.open_addressing_hash_map.HashMap(capacity)

    def add(self, value):
        self.l.put(value, None)

    def get(self, value):
        return self.l._get(value).key

    def size(self):
        return self.l.size()
