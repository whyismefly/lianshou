#!/usr/bin/python
# encoding:utf_8

a = int(input('请输入任意一个的正整数：'))
count = 0
# 用while循环，直到最后的a小于1时，便计数完毕
while (a >= 1):
    num_daoxu = int(a % 10)
    print(num_daoxu)
    a /= 10
    count += 1
print('它是%d位数。'%count)