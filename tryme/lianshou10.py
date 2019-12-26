#!/usr/bin/python
# encoding:utf_8

# 第十一题 判断101-200之间有多少个素数，并输出所有素数。

import math
count=0
for i in range(101,201):
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            break
        elif j==int(math.sqrt(i)):
            count+=1
            print (i)
print(count)


# count = 0
# for i in range(101, 201):
#     # 因为下文涉及到了，循环+判断，所以必须要引入一个值来记录：所有循环满足条件？还是部分符合条件？
#     # a的值可以看作标记。
#     a = 0
#     for j in range(2, int(math.sqrt(i)+1)):
#         if i % j == 0:
#             a = 1
#     # 在一个i值下，循环了j值。如果依旧a==0,就说明满足条件素数条件
#     if a == 0:
#         count += 1
#         print(i)
# print('一共有'+str(count)+'个。')