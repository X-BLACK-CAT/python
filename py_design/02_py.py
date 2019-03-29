'''
题目描述
    打印所有不超过n（n<256）的，其平方具有对称性质的数。如11*11=121。
输入描述:
    无
输出描述:
    每行一个数，表示对称平方数。
'''
def f(n):
    flag = True
    sum = n * n
    sum_str_list = [i for i in str(sum)]
    a, b = divmod(len(str(sum)), 2)
    for i in range(0,len(sum_str_list)//2):
        if b > 0:
            if sum_str_list[len(sum_str_list)//2-i-1] == sum_str_list[len(sum_str_list)//2+i+1]:
                continue
            else:
                flag = False
                break
        else:
            if sum_str_list[len(sum_str_list)//2-i-1] == sum_str_list[len(sum_str_list)//2+i]:
                continue
            else:
                flag = False
                break
    if flag:
        print(n)

    else:
        pass


if __name__ == '__main__':
    for i in range(1, 257):
        f(i)