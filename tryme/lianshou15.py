#!/usr/bin/python3
# encoding:utf_8

# 第十五题 一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3。

# 首先，先设置1000以内的数循环

for wanshu in range(2,10001):
    a=0
    yinzi=[]
    i=wanshu
    while (i!=1):
        for y in range(2, int(i + 1)):
            if i%y==0:
                i/=y
                yinzi.append(y)
                break
    for z in range(0,len(yinzi)):
        a+=yinzi[z]
    if (a+1)==wanshu:
        print(wanshu)

# for wanshu in range(2, 1001):
#     a = 0
#     # 建立列表，保存因子
#     yinzi = []
#     i = wanshu
#     # 设置内循环，找出所有因子（前面题目有详细解释）
#     while (i != 1):
#         for y in range(2, int(i+1)):
#             if i % y == 0:
#                 i /= y
#                 yinzi.append(y)
#                 break
#     # 求出列表里所有数的和
#     for z in range(0, len(yinzi)):
#         a += yinzi[z]
#     # 不要忘记1
#     if (a+1) == wanshu:
#         print(wanshu)