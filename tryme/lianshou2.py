#!/usr/bin/python
# encoding:utf_8

import re
# 第三题 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# 统计字母、空格、数字这些东西，能迅速把他们进行分类的，只有正则表达式
# 正则表达式挑选符合要求的数字，以后爬虫也会经常遇到，就当练手

import re
a = raw_input('请输入一串字符：')
# 注意不要忽略了引号
# re.compile()编译正则表达式，生成正则表达式对象
zimu = re.compile('[a-zA-Z]')
kongge = re.compile(r'\s')
shuzi = re.compile(r'\d')
# findall()函数可以找到任何满足正则表达式条件的内容，并生成一个列表
count_shuzi = len(shuzi.findall(a))
count_zimu = len(zimu.findall(a))
count_kongge = len(kongge.findall(a))
count_qita = len(a) - count_kongge - count_zimu - count_shuzi
print('英文字母个数为：%d'%count_zimu)
b=shuzi.findall(a)
print (b)
print('空格个数为：%d'%count_kongge)
print('数字个数为：%d'%count_shuzi)
print('其他个数为：%d'%count_qita)