#!/usr/bin/python3
# encoding:utf_8

# 第二十题 对10个随机个位数进行排序（从小到大）。

import random

# list1=[]
# for i in range(0,10):
#     x=random.randrange(0,100)
#     list1.append(x)
list1=[random.randrange(0,10) for i in range(0,10)]
print(list1)
list1.sort()
print(list1)

# # 笔者最后拿这个题目镇文章哈
# # 第一种方法，利用循环
# # 首先，利用random生成十个随机数
# import random
# list_num = [random.randint(0, 10) for i in range(0, 10)]
# print('需要排列的数据列表为', list_num, '。')
# # 建立空列表存储排列好的值
# sorted_list_num = []
# # 加入一个数，作为基数，和其他几个数比较
# sorted_list_num.append(list_num[0])
# for i in range(1, 10):
#     a = i
#     for m in range(i, 0, -1):
#         # 如果要加入的数大于前一个数，则将其放在该数后面
#         if list_num[a] > sorted_list_num[(m - 1)]:
#             sorted_list_num.insert(m, list_num[a])
#             break
#         # 如果小于的话，重新循环
#         else:
#             # 若是最小数的话，则放在首位
#             if m == 1:
#                 sorted_list_num.insert(0, list_num[a])
#                 break
# print('排好的序列为：', sorted_list_num, '。')
#
# #第二种方法 和第一种方法大同小异，只不过是笔者想联系函数的思想
# import random
# list_num = [random.randint(0, 10) for i in range(0, 10)]
# print('需要排列的数据列表为', list_num, '。')
# sorted_list_num = []
# sorted_list_num.append(list_num[0])
# def sort_method(i):
#     a = i
#     # global 定义全局变量很重要
#     global sorted_list_num
#     for m in range(i, 0, -1):
#         if list_num[a] > sorted_list_num[(m - 1)]:
#             sorted_list_num.insert(m, list_num[a])
#             # return 返回函数，表明函数结束
#             return
#         else:
#             if m == 1:
#                 sorted_list_num.insert(0, list_num[a])
#                 # return 返回函数，表明函数结束
#                 return
#
# for i in range(1, 10):
#     sort_method(i)
# print('排好的序列为：', sorted_list_num, '。')