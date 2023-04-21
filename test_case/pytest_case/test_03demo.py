import unittest

from .utils import ddt, data

data_list = ['test', 'test1', 'test3', 'test4', 'test5']


@ddt
class MyTestCase(unittest.TestCase):
    @data(*data_list)
    def test_something(self, itme):
        print(itme)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
