import unittest


def count_digits(value):
    if value == 0:
        return 0
    return 1 + count_digits(int(value / 10))


class DigitsCounterTest (unittest.TestCase):
    def test(self):
        self.assertEqual(9, count_digits(123456789))

    def test15(self):
        self.assertEqual(2, count_digits(15))

    def test105(self):
        self.assertEqual(3, count_digits(105))

    def test15105(self):
        self.assertEqual(5, count_digits(15105))

    def testLessThan10(self):
        self.assertEqual(1, count_digits(1))

    def test0(self):
        self.assertEqual(0, count_digits(0))
