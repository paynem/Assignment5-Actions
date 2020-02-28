import unittest
import task


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


if __name__ == '__main__':
    unittest.main()
