# -*- coding:utf-8 -*-


def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    # 控制要移动多少趟
    for j in range(n-1): # o(n^2)
        # 班长从头走到尾
        count = 0
        for i in range(0, n-j-1):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
            print(alist)
        if count == 0:
            return


if __name__ == "__main__":
    li = [2, 1, 15, 16, 17, 8]
    print(bubble_sort(li))
    print(li)
    for j in range(len(li) - 1, 0, -1):
        print(j,end=" ")

