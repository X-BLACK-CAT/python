# -*- coding:utf-8 -*-

# from abc import ABCMeta,abstractmethod
#
# class Payment(metaclass=ABCMeta):
#     @abstractmethod#定义抽象方法的关键字
#     def pay(self,money):
#         pass
#
#     # @abstractmethod
#     # def pay(self,money):
#     #     raise NotImplementedError
#
# class AiliPay(Payment):
#     #子类继承接口,必须实现接口中定义的抽象方法,否则不能实例化对象
#     def pay(self,money):
#         print('使用支付宝支付%s元'%money)


'''单例设计模式'''
# class Singleton(object):
#     # 如果该类已经有了一个实例直接返回，否则创建一个全局唯一的实例
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls,'_instance'):
#             cls._instance = super(Singleton,cls).__new__(cls)
#         return cls._instance
#
# class MyClass(Singleton):
#     def __init__(self,name):
#         if name:
#             self.name = name
#
# a = MyClass('a')
# print(a)
# print(a.name)
# b = MyClass('b')
# print(b)
# print(b.name)
# a,b = divmod(2,2)
# print(a,b)
a_list = ['1','2','3','4']


def get_num_list(num,arg):
    arg.remove(num)
    return arg

for a in a_list:
    for b in get_num_list(a,a_list.copy()):
        if b == a:
            continue
        else:
            for c in get_num_list(b,a_list.copy()):
                if c == a or c == b :
                    continue
                else:
                    print(c + a + b)
                    print(a + c + b)
                    print(c + b + a)
                    print(a + b + c)
                    print(b + a + c)
                    print(b + c + a)



