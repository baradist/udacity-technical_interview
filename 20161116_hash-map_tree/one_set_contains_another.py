import unittest
import collects.hash_set


class OneSetContainsAnotherTest (unittest.TestCase):
    def test(self):
        set_s = collects.hash_set.HashSet(10)
        set_s.add(1)
        set_s.add("two")

        set_t = collects.hash_set.HashSet(10)
        set_t.add(1)
        set_t.add("two")
        set_t.add("three")

        size_before = set_t.size()
        set_t.add_all(set_s)
        size_after = set_t.size()
        self.assertEqual(size_before, size_after)

    def testNegative(self):
        set_s = collects.hash_set.HashSet(10)
        set_s.add(1)
        set_s.add("four")

        set_t = collects.hash_set.HashSet(10)
        set_t.add(1)
        set_t.add("two")
        set_t.add("three")

        set_t.l.size()
        size_before = set_t.size()
        self.assertEqual(3, size_before)

        set_t.add_all(set_s)
        size_after = set_t.size()
        self.assertEqual(4, size_after)
