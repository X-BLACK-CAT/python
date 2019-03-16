# -*- coding:utf-8 -*-


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    for j in range(1,n):
        # j 内层循化的取值
        i = j
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -= 1
            else:
                break


if __name__ == "__main__":
    li = [54, 226, 93, 17,40, 77, 31, 44, 55, 20]
    insert_sort(li)
    print(li)