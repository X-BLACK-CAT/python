import sys

# for line in sys.stdin:
#     str_list = line.split()

def get_add_days(sum_days,days,total_days,date_list):
    for i in range(days, date_list):
        if sum_days + 1 < total_days:
            sum_days += 1
        else:
            return i

def fun(arg):
    date_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    year,month,days,add_days = int(arg.split()[0]),int(arg.split()[1]),int(arg.split()[2]),int(arg.split()[3])
    flag = is_leap_year(year)
    if flag:
        date_list[1] = 29
    else:
        date_list[1] = 28

    sum_days = get_sum_days(month,days,date_list)
    total_days = sum_days + add_days
    for date in date_list[month:-1]:

        if sum_days+date <= total_days:
            sum_days += date
            month += 1
            if month > 12:
                month = 1
                year += 1
                for date in date_list:
                    if sum_days <= total_days:
                        sum_days += date
                        month += 1
                    else:
                        days = get_add_days(sum_days, days, total_days, date_list[month])
                        print(str(year) + '-' + str(month) + '-' + str(days))
                        break
            else:
                continue
        else:
            days = get_add_days(sum_days,days,total_days,date_list[month])
            print(str(year) + '-' + str(month) + '-' + str(days))
            break



def is_leap_year(year):
    if year%4==0 and year%100!=0 and year%400==0:
        flag = True
    else:
        flag = False
    return flag

def get_sum_days(month,days,date_list):
    sum_days = 0
    for date in date_list[0:month]:
        sum_days += date
    sum_days += days
    return sum_days


if __name__ == '__main__':
    n = sys.stdin.readline().strip()

    for i in range(int(n)):
        in_str = sys.stdin.readline().strip()
        fun(in_str)

# import datetime
#
# m = input()
# time_set = []
# for i in range(int(m)):
#     temp = input().split()
#     time_set.append(temp)
#
# for temp_time in time_set:
#     time1 = datetime.date(int(temp_time[0]), int(temp_time[1]), int(temp_time[2]))
#     time2 = time1 + datetime.timedelta(days=int(temp_time[3]))
#     print(time2)