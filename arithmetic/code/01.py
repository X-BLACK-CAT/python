# -*- coding:utf-8 -*-

"""如果 a+b+c=1000，且 a^2+b^2=c^2（a,b
,c 为自然数），如何求出所有a、b、c可能的组合?"""
# 枚举法
# a
# b
# c
# c = 1000 - a -b
"""时间复杂度"""
# T = 1000 * 1000 * 1000 * 2
# T = N * N * N * 2
# T (n) = n^3*2

# import time
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2 + b**2 == c**2:
#                 print("a=%d b=%d c=%d "%(a,b,c))
# end_time = time.time()
# print("times:%d"%(end_time-start_time))
# print("finished")

# 每台机器的执行总时间不同 ，但是执行基本运算数量大体相同
# import time
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000 - a - b
#         if a+b+c == 1000 and a**2 + b**2 == c**2:
#             print("a=%d b=%d c=%d "%(a,b,c))
# end_time = time.time()
# print("times:%d"%(end_time-start_time))
# print("finished")

"""排序法"""

# li = [11,31,4,7,5,14,16,9]
# li.sort()
# print(li)

a = 20
b = 10
a,b = b,a
print(a,b)
