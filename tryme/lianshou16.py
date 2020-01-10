#!/usr/bin/python3
# encoding:utf_8

# 第十六题 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

height=100
s=height
cishu=10
for i in range(1,cishu+1):
    height=height/2
    s+=2*height
print(height)
print(s)


# s = 100
# h = 50
# distance = 0
# for i in range(0, 10):
#     distance += (s + h) * 0.5 ** i
# print('经过的路程为%f米。'%distance)
# high = s * 0.5 ** 10
# print('第十次反弹的高度为%f米。'%high)
