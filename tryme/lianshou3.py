#!/usr/bin/python
# encoding:utf_8

# 第四题 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定
# 比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

# 这道题用到很多重新赋值，以及列表删除方法
# 首先注意a不能直接赋值

team_jia = [str('a'), str('b'), str('c')]
# 第一个循环确定a和谁比赛，
for i in range(0, 3):
    team_yi = [str('x'), str('y'), str('z')]
    match_list = []
    selected_first_yi = team_yi.pop(i)
    if selected_first_yi != 'x':
        # 第二个循环，产生接下来的两场比赛
        for j in range(0, 2):
            # 由于后面又用到了list.pop()，因此要重新赋值
            team_yi = [str('x'), str('y'), str('z')]
            team_yi.remove(selected_first_yi)
            # 重新赋值
            match_list = [tuple([team_jia[0], selected_first_yi])]
            match_list.append(tuple([team_jia[1], team_yi.pop(j)]))
            # 两次pop()后，team_yi只剩下一个值
            match_list.append(tuple([team_jia[2], team_yi[0]]))
            if ('c', 'x') not in match_list and ('c', 'z') not in match_list :
                print("比赛顺序为:", match_list, '.')

# list1=[0,1,2,3,4,5,6]
# for i in range(len(list1)):
#     print (list1.pop())
#     print (list1)