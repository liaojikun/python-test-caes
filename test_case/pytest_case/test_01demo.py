from .utils import ddt, data

data_list = ['test', 'test1', 'test3', 'test4', 'test5']


@ddt
class TestDemo:

    @data(*data_list)
    def test_demo(self, item):
        print(item)
        assert 0 == 0
