#!/usr/bin/python3
# encoding:utf_8

# 第十七题 猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个，第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少？
i=1
day=10
for j in range(1,day):
    i=(i+1)*2
    print(i)

# num_taozi = 1
# for i in range(1, 10):
#     num_taozi = (num_taozi + 1) * 2
# print('桃子总个数为%d个。'%num_taozi)