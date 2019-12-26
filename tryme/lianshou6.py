#!/usr/bin/python
# encoding:utf_8

# 第七题 输入某年某日 判断你这是第几天？

import datetime

input_year = int(input('year:'))
input_month = int(input('month:'))
input_day = int(input('day:'))
# 这里要用到int()函数，确保是整数
# 下面的调用，是最简单的求时间差异的方法
time1 = datetime.datetime(input_year, input_month, input_day)
time2 = datetime.datetime(input_year, 1, 1)
days = (time1-time2).days+1
print('这是第%d天。'%days)