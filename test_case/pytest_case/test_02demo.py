import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_something_01(self):
        self.assertEqual(True, True)

    def test_something_02(self):
        self.assertEqual(True, True)

    def test_something_03(self):
        self.assertEqual(True, False)

    def test_something_04(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
