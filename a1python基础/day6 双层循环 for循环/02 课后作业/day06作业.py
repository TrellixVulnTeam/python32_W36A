# ''''''
# '''

1.利用if语句写出猜大小的游戏：
	设定一个理想数字比如：66，
	让用户三次机会猜数字，如果比66大，则显示猜测的结果大了；
	如果比66小，则显示猜测的结果小了;
	只有等于66，显示猜测结果正确，退出循环。
	最多三次都没有猜测正确，退出循环，并显示‘都没猜对,继续努力’。

2.使用while和for 遍历字符串 "IG战队牛逼"
3.使用for循环对s="黄绿青蓝紫"进行循环，每次打印的内容是每个字符加上"色的"，
  例如：黄色的 绿色的 青色的 ...
4.完成要求：
用户可持续输入(while循环)
	输入A，则显示走大路回家，然后在让用户进一步选择：
		是选择公交车，还是步行？
		选择公交车，显示10分钟到家，并退出整个程序。
		选择步行，显示20分钟到家，并退出整个程序。
	输入B，
		则显示走小路回家，并退出整个程序。
	输入C，
		则显示绕道回家，然后在让用户进一步选择：
		是选择游戏厅玩会，还是网吧？
			选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
			选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。

5.写代码：计算 1 - 2 + 3 - 4 + ... + 99 中除了88以外所有数的总和？
6.(升级题)打印菱形小星星
     *
    ***
   *****
  *******
 *********
***********
***********
 *********
  *******
   *****
    ***
     *
# '''

# 1.利用if语句写出猜大小的游戏：
# 	设定一个理想数字比如：66，
# 	让用户三次机会猜数字，如果比66大，则显示猜测的结果大了；
# 	如果比66小，则显示猜测的结果小了;
# 	只有等于66，显示猜测结果正确，退出循环。
# 	最多三次都没有猜测正确，退出循环，并显示‘都没猜对,继续努力’。

# times = 0
# for i in range(3):
# 	guess = int(input('请猜数:'))
# 	if guess > 66:
# 		print('猜大了')
# 	elif guess < 66:
# 		print('猜小了')
# 	elif guess == 66:
# 		print('猜对了')
# 		break
# 	times += 1
# 	print('你还有%s次机会' % (3-times))
# else:
# 	print('都没猜对,继续努力')

# 2.使用while和for 遍历字符串 "IG战队牛逼"
strvar = 'IG战队牛逼'
#方法1 while
i = 0
while i < len(strvar):
	print(strvar[i])
	i += 1
print('--------------------2-1')

#方法2 for
for i in strvar:
	print(i)
print('--------------------2-2')

# 3.使用for循环对s="黄绿青蓝紫"进行循环，每次打印的内容是每个字符加上"色的"，
#   例如：黄色的 绿色的 青色的 ...
strvar = '黄绿青蓝紫'
for i in strvar:
	print(i+'色的')
print('--------------------3-1')

# 4.完成要求：
# 用户可持续输入(while循环)
# 	输入A，则显示走大路回家，然后在让用户进一步选择：
# 		是选择公交车，还是步行？
# 		选择公交车，显示10分钟到家，并退出整个程序。
# 		选择步行，显示20分钟到家，并退出整个程序。
# 	输入B，
# 		则显示走小路回家，并退出整个程序。
# 	输入C，
# 		则显示绕道回家，然后在让用户进一步选择：
# 		是选择游戏厅玩会，还是网吧？
# 			选择游戏厅，则显示 ‘一个半小时到家，爸爸在家，拿棍等你。’并让其重新输入A，B,C选项。
# 			选择网吧，则显示‘两个小时到家，妈妈已做好了战斗准备。’并让其重新输入A，B,C选项。

# i = 0
sign = True
while sign:
	choice = input('请选择回家方式,A(走大路回家) B(走小路回家) C(绕道回家):')
	if choice == 'A':
		print('请走大路回家')
		while True:
			choice2 = input('是选择公交车(g),还是步行(b)?')
			if choice2 == 'g':
				print('10分钟到家')
				sign = False
				break   #跳出内循环
			elif choice2 == 'b':
				print('20分钟到家')
				sign = False
				break
			else:
				print('输入错误,请输入g b')
	elif choice == 'B':
		print('走小路回家')
		break  #跳出外循环
	elif choice == 'C':
		print('绕道回家')
		while True:
			choice3 = input('是选择游戏厅玩会(y)，还是网吧(w)?')
			if choice3 == 'y':
				print('一个半小时到家，爸爸在家，拿棍等你')
				break  #跳出内循环
			elif choice3 == 'w':
				print('两个小时到家，妈妈已做好了战斗准备')
				break  #跳出内循环
			else:
				print('输入错误,请输入y w')
				continue  #跳出内循环的当次循环
	else:
		print('输入错误,请输入A B C')

# 5.写代码：计算 1 - 2 + 3 - 4 + ... + 99 中除了88以外所有数的总和？
i = 1
total_ji = 0
while i <= 99:
	if i % 2 == 1:
		total_ji += i
	i += 1
print(total_ji)

i = -2
total_ou = 0
while i >= -98:
	if i % 2 == 0:
		total_ou += i
	i -= 1
print(total_ou)

total  = total_ji + total_ou +88
print(total)   # 138
print('---------------------------------5-1')

# 用这个
total = 0
for i in range(1,100):
	if i % 2 == 1:
		total += i
	elif i % 2 == 0:
		if i == 88:
			continue
		total -= i
print(total)
print('---------------------------------5-2')

# 6.(升级题)打印菱形小星星








