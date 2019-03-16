# -*- coding:utf-8 -*-
arr = [1, 3, 6, 9, 15,10,5, 20, 30]


def findnumber(l, h, number):
    mid = (l + h) // 2
    if arr[mid] == number:
        print("找到了" + str(mid))
    elif arr[mid] < number:
        l = mid
        return findnumber(mid + 1, h, number)
    elif arr[mid] > number:
        h = mid
        return findnumber(0, mid - 1, number)
    else:
        print("没有找到")


findnumber(0, len(arr) - 1, 30)


def binary_search(data_source, find_n):
    # 取中位数
    mid = int(len(data_source) / 2)

    if len(data_source) >= 1:
        if data_source[mid] > find_n:  # 中位数大于要查找的数，则要查找的数在左半部分，继续调用二分算法进行查找
            binary_search(data_source[:mid], find_n)
        elif data_source[mid] < find_n:  # 中位数小于要查找的数，则要查找的数在右半部分
            binary_search(data_source[mid:], find_n)
        else:  # 中位数等于要查找的数
            print("找到了：", data_source[mid])
    else:
        print("没有找到")


data = list(range(1, 100001))
binary_search(data, 6)

