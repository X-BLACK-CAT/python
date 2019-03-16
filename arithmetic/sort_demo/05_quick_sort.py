# -*- coding:utf-8 -*-


def quick_sort(alist,begin,end):
    """快速排序"""
    if begin >= end:
        return
    mid_value = alist[begin]
    low = begin
    high = end
    while low < high:
        # high左移
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]
        print(alist)
        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]
        print(alist)
    # 循环退出时low==high
    alist[low] = mid_value
    print(alist[low])
    # 对low左边的列表进行快排
    quick_sort(alist,begin,low-1)
    # 对low右边的列表进行快排
    quick_sort(alist,low+1,end)


if __name__ == "__main__":
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20,78,35,89,15]
    n = len(li)-1
    quick_sort(li,0,n)
    print(li)