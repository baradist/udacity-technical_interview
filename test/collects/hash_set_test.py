import unittest
import collects.hash_set


class HashSetTest (unittest.TestCase):
    def test(self):
        set = collects.hash_set.HashSet(10)
        set.add(1)
        set.add(11)
        set.add("two")
        set.add("two") # "two again" should replace "two"

        self.assertEqual(1, set.get(1))
        self.assertEqual(11, set.get(11))
        self.assertEqual("two", set.get("two"))
        self.assertEqual(3, set.size())

    def test_overflow(self):
        set = collects.hash_set.HashSet(4)
        set.add(7 )
        set.add(17)
        set.add(27)
        set.add(37)

        with self.assertRaises(Exception):
            set.add(47)
