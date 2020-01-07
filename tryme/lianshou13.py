#!/usr/bin/python3
# encoding:utf_8

#第十三题 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

# while True:
#     your_grade = int(input('你的学习成绩为：'))
#     mark = your_grade >= 90 and 'A' or your_grade >= 60 and 'B' or 'C'
#     print('你的成绩类型是%s.'%mark)

while True:
    grade=int(input("grade:"))
    mark = grade >= 90 and "a" or grade >= 60 and 'b' or 'c'
    print("mark:",mark)