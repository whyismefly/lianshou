#!/usr/bin/python3
# encoding:utf_8

# 第十八题 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

x=2
y=1
z=x/y
list1=[]
cishu=20
for i in range(1,cishu+1):
    list1.append(z)
    # a=x
    # b=x+y
    # x=b
    # y=a
    x,y=x+y,x
    z = x / y
sum1=sum(list1)
print(sum1)

# # 一个数的分子是前一个数分子和分母之和
# # 并且，这个数的分母是前一个数的分子
# # 其中，用到到斐波那契数列的构造思想
# a = 2
# b = 1
# s = 0
# for i in range(0, 20):
#     s += a/b
#     # 其中，用到到斐波那契数列数列的构造思想
#     a, b = a + b, a
# print(s)