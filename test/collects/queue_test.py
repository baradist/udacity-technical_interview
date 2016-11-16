import unittest
import collects.queue


class QueueTest (unittest.TestCase):
    def test(self):
        queue = collects.queue.Queue()
        self.assertEqual(True, queue.is_empty())

        queue.add("one")
        self.assertEqual("one", queue.peek())
        self.assertEqual(1, queue.size())

        queue.add("two")
        queue.add("three")
        self.assertEqual(False, queue.is_empty())
        self.assertEqual(queue.size(), 3)

        self.assertEqual("one", queue.poll())
        self.assertEqual("two", queue.poll())
        self.assertEqual("three", queue.poll())
        self.assertEqual(True, queue.is_empty())
