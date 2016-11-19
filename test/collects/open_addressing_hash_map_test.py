import unittest
import collects.open_addressing_hash_map


class HashMapTest (unittest.TestCase):
    def test(self):
        map = collects.open_addressing_hash_map.HashMap(10)
        map.put(1, "one")
        map.put(11, "another one")
        map.put("two", "two")
        map.put("two", "two again") # "two again" should replace "two"

        self.assertEqual("one", map.get(1))
        self.assertEqual("another one", map.get(11))
        self.assertEqual("two again", map.get("two"))

    def test_overflow(self):
        map = collects.open_addressing_hash_map.HashMap(4)
        map.put(7, "something")
        map.put(17, "something")
        map.put(27, "something")
        map.put(37, "something")

        with self.assertRaises(Exception):
            map.put(47, "something")

    def testPutAll(self):
        map = collects.open_addressing_hash_map.HashMap(10)
        new_map = collects.open_addressing_hash_map.HashMap(10)
        map.put(1, "one")
        map.put(11, "another one")
        map.put("two", "two")
        map.put("two", "two again")  # "two again" should replace "two"
        new_map.put_all(map)

        self.assertEqual("one", new_map.get(1))
        self.assertEqual("another one", new_map.get(11))
        self.assertEqual("two again", new_map.get("two"))
