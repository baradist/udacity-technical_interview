import unittest
import copy


def sort(list):
    _sort(list, copy.copy(list), 0, len(list) - 1)


def _sort(list, aux_list, lo, hi):
    if hi <= lo:
        return
    mid = int(lo + (hi - lo) / 2)
    _sort(list, aux_list, lo, mid)
    _sort(list, aux_list, mid + 1, hi)
    _merge(list, aux_list, lo, mid, hi)


def _merge(list, aux_list, lo, mid, hi):
    for k in range(lo, hi + 1):
        aux_list[k] = list[k]

    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            list[k] = aux_list[j]
            j += 1
        elif j > hi:
            list[k] = aux_list[i]
            i += 1
        elif aux_list[j] < aux_list[i]:
            list[k] = aux_list[j]
            j += 1
        else:
            list[k] = aux_list[i]
            i += 1


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
