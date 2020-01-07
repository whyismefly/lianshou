#!/usr/bin/python3
# encoding:utf_8

# 第十四题 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字，有几个数相加由自己来控制。例如输出：2+22+222+2222+22222(此时共有5个数相加)并求值。

a=int(input("a:"))
num=int(input("num:"))
b=0
c=0
for i in range(0,num):

    b=b*10+a
    c=c+b
    print(b,c)


# a = int(input('输入你的a值：'))
# b = int(input('你想让几个数相加：'))
# s = 0
# print('s=', end=' ')
# # 开始循环每个加数
# for i in range(0, b):
#     # 初始化d值
#     d = 0
#     # 实现每个加数
#     for y in range(0, i+1):
#         c = a*10**y
#         d += c
#     # 设置输出的格式
#     if d < 10**(b - 1):
#         print(d, '+', end=' ')
#     else:
#         print(d, end='')
#     s += d
# print(' =', s)