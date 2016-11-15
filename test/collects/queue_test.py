import unittest
import collects.queue


class QuereTest (unittest.TestCase):
    def test(self):
        queue = collects.queue.Queue()
        self.assertEqual(queue.is_empty(), True)

        queue.add("one")
        self.assertEqual(queue.peek(), "one")
        self.assertEqual(queue.size(), 1)

        queue.add("two")
        queue.add("three")
        self.assertEqual(queue.is_empty(), False)
        self.assertEqual(queue.size(), 3)

        self.assertEqual(queue.poll(), "one")
        self.assertEqual(queue.poll(), "two")
        self.assertEqual(queue.poll(), "three")
        self.assertEqual(queue.is_empty(), True)
