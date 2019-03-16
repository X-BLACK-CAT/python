# -*- coding:utf-8 -*-


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2  # 取整 python3
    # 控制gap的步长
    while gap >= 1:
        # 插入算法，与普通的插入算法的区别就是gap步长
        for j in range(gap,n):
            i = j
            while i > 0:
                if alist[i]<alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                    print(i)
                else:
                    break
        # 缩短步长
        gap //= 2


if __name__ == "__main__":
    li = [54,26,93,17,77,31,44,55,20]
    shell_sort(li)
    print(li)
    n = len(li)
    print((n //2))