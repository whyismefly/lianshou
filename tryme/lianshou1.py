#!/usr/bin/python
# encoding:utf_8

#https://zhuanlan.zhihu.com/p/35499854

count = 0
num_list = []
for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and k != i:
                count += 1
                num_list.append(100 * i + 10 * j + k)
print(count)
print("这些数字为：", num_list)