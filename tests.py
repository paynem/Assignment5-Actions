import unittest
import task
from datetime import date


class TestCase(unittest.TestCase):

    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test3(self):
        expected = 78.5
        self.assertEqual(expected, task.circleArea(5))

    def test4(self):
        expected = 500
        self.assertNotEqual(expected, task.circleArea(6))

    def test5(self):
        theList = [1, 2, 3, 4, 5]
        first, last = task.listInfo(theList)
        self.assertEqual(theList[0], first)
        self.assertEqual(theList[-1], last)

    def test6(self):
        theList = [1, 2, 3, 4, 5]
        last, first = task.listInfo(theList)
        self.assertNotEqual(theList[0], first)
        self.assertNotEqual(theList[-1], last)

    def test7(self):
        a = date(2020, 2, 28)
        b = date(2020, 3, 15)
        expected = 16
        self.assertEqual(expected, task.dateTime(a, b))

    def test8(self):
        a = date(2020, 2, 2)
        b = date(2020, 2, 23)
        expected = 14
        self.assertNotEqual(expected, task.dateTime(a, b))


if __name__ == '__main__':
    unittest.main()
