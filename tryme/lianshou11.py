#!/usr/bin/python
# encoding:utf_8

# 第十二题 打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。

import math

for i in range(152,1000):
    gewei=i%10
    shiwei=(i%100-gewei)/10
    baiwei=int(i/100)
    if i==gewei**3+shiwei**3+baiwei**3:
        print (i)

# for a in range(100, 1000):
#     b = a//100
#     c = (a - 100*b)//10
#     d = a - 100*b-10*c
#     if a == b**3 + c**3 + d**3:
#         print(a)
