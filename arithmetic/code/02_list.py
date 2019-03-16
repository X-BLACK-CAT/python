# -*- coding:utf-8 -*-
import timeit

# li1 = [1,2]
#
# li2 = [23,5]
# li = li1+li2
# li = [i for i in range(10000)]
# li = list(range(10000)) # range(10000)返回可迭代的对象


def test1():
    li = []
    for i in range(10000):
        li.append(i)


def test2():
    li = []
    for i in range(10000):
        li += [i]


def test3():
   li = [i for i in range(10000)]


def test4():
    li = list(range(10000))


def test5():
    li = []
    for i in range(10000):
        li.extend([i])


timer1 = timeit.Timer("test1()","from __main__ import test1")
print("append",timer1.timeit(1000))
timer2 = timeit.Timer("test2()","from __main__ import test2")
print("+:",timer2.timeit(1000))
timer3 = timeit.Timer("test3()","from __main__ import test3")
print("[i for i in range]",timer3.timeit(1000))
timer4 = timeit.Timer("test4()","from __main__ import test4")
print("list(range)",timer4.timeit(1000))
timer5 = timeit.Timer("test5()","from __main__ import test5")
print("extend([i])",timer5.timeit(1000))


def t6():
    li = []
    for i in range(10000):
        li.append(i)


def t7():
    li = []
    for i in range(10000):
        li.insert(0,i)