#!/usr/bin/python
# encoding:utf_8

# 第六题 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

import math

x=1
y=True
while y:
    if math.sqrt(x+100)==int(math.sqrt(x+100)) and math.sqrt(x+168) == int(math.sqrt(x+168)):
        print x
        y=False
    x+=1

# x = 1
# while True:
#     if math.sqrt(x+100) - int(math.sqrt(x+100)) == 0 and math.sqrt(x+168) - int(math.sqrt(x+168)) == 0:
#         print(x)
#         # 只求一个整数，则要在找到这个整数的时候，加入一个break，表示退出循环
#         break
#     # 如果不满足条件，x+1进行继续循环判断
#     x += 1