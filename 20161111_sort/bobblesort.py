import unittest


def sort(list):
    size = len(list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, size):
            if list[i - 1] > list[i]:
                swapped = True
                tmp = list[i - 1]
                list[i - 1] = list[i]
                list[i] = tmp


class SortTest (unittest.TestCase):
    def testSome(self):
        print("testSome")

        list = [2, 1, 3, 0]
        print(list)

        sort(list)
        print(list)

        self.assertEqual(0, list[0])
        self.assertEqual(1, list[1])
        self.assertEqual(2, list[2])
        self.assertEqual(3, list[3])

    def testSmall(self):
        print("testSmall")

        list = [1, 3]
        print(list)

        sort(list)
        print(list)

        self.assertEqual(1, list[0])
        self.assertEqual(3, list[1])

    def testEmpty(self):
        print("testEmpty")

        list = []
        print(list)

        sort(list)
        print(list)

        self.assertEqual(0, len(list))

    def testOdd(self):
        print("testOdd")

        list = [2, 1, 3, 0, 5]
        print(list)

        sort(list)
        print(list)

        self.assertEqual(0, list[0])
        self.assertEqual(1, list[1])
        self.assertEqual(2, list[2])
        self.assertEqual(3, list[3])
        self.assertEqual(5, list[4])
