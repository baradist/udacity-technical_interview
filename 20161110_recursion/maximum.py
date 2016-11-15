import collects.linked_list
import unittest


def max_in_list(list):
    if list.is_empty():
        return float('-inf')
    return max(list.remove_first(), max_in_list(list))


class MaxTest (unittest.TestCase):
    def test(self):
        list = collects.linked_list.LinkedList()
        list.add_first(10)
        list.add_first(2)
        list.add_first(42)
        list.add_first(7)

        value = max_in_list(list)
        print(value)
        self.assertEqual(42, value)

    def testNegative(self):
        list = collects.linked_list.LinkedList()
        list.add_first(-10)
        list.add_first(-2)
        list.add_first(-4)
        list.add_first(-7)

        value = max_in_list(list)
        print(value)
        self.assertEqual(-2, value)
