
def create_func(func, data):
    def wrapper(self):
        func(self, data)
    return wrapper


def data(*args):
    def wrapper(func):
        setattr(func, 'DATA', args)
        return func
    return wrapper


def ddt(cls):
    # 遍历测试测试类所有的方法和属性
    for name, func in list(cls.__dict__.items()):
        # 判断遍历出来的方法/属性是否保存了测试数据（被data装饰器装饰过）
        if hasattr(func, 'DATA'):
            print(name, func)
            # 遍历测试数据，动态给类设置测试方法
            for index, value in enumerate(func.DATA):
                func_name = '{}_{}'.format(name, index+1)
                # 通过闭包创建一个方法。
                new_func = create_func(func, value)
                # 动态添加一个方法
                setattr(cls, func_name, new_func)
            # 循环遍历测试数据，添加完方法之后，除原来类中定义的方法
            delattr(cls, name)
    return cls
