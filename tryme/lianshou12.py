#!/usr/bin/python
# encoding:utf_8

# 第十三题 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5

import math

num=input("num:")
while num!=1:
    for i in range(2,num+1):
        if num%i==0:
            num/=i
            if num==1:
                print (i,),
            else:
                print (i,'*',),
                break


# a = int(input('您要将哪个数分解为质因数相乘的形式：'))
# print(a, '=', ),
# while (a != 1):
#     # 注意对除数的循环要从2开始，从1开始会陷入死循环
#     for i in range(2, int(a+1)):
#         if a % i == 0:
#             # 这个地方很重要，提取完a的最小后的现值，再赋予a，这个时候就需要/=
#             a /= i
#             if a == 1:
#                 print(i, ),
#             else:
#                 print(i, '*', ),
#                 # 最深层次的if循环语句是为了打印输出结果
#                 # 但是，我们还要在这个现值a上重新开始for循环，而不是继续开始for循环
#                 # 这时候，就可以使用break跳出for循环，去验证while条件句
#                 # 如果不是最简，则重新开始for循环，并使用新的a值
#                 break
