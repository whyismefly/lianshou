#!/usr/bin/python
# encoding:utf_8

# 第九题 输出9*9口诀表，注意输出形式为直角三角形。

# for i in range(1,10):
#     for j in range(1,10):
#         if i<=j:
#             x=i*j
#             if j!=9:
#                 print(i,"*",j,"=",x),
#             else:
#                 print(i,"*",j,"=",x)



for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print(j, "*", i, "=", i*j," "),
    # 下一行代码代表着内置循环结束以后，在输出一个’‘，其实这是什么都没有的，只是没有end=’‘，所以就自动换行了
    print('')
