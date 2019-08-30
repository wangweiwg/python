# 循环结构：控制某件事或者某些事重复、重复、再重复的去执行
# 在Python中构造循环结构有两种做法，一种是for-in循环，一种是while循环


# for-in循环
# 如果明确的知道循环执行的次数或者要对一个容器进行迭代，推荐使用for-in循环，
# 计算 1 ~ 100 求和的结果
sum = 0
for x in range(0, 100, 2):
	print(x)
# range类型，range可以用来产生一个不变的数值序列，而且这个序列通常都是用在循环中的
# range(101)可以产生一个0到100的整数序列
# range(1, 100)可以产生一个1到99的整数序列
# range(1, 100, 2) 可以产生一个1到99的奇数序列，其中的2是步长，即数值序列的增量



# while循环
# 如果要构造不知道具体循环次数的循环结构，推荐使用while循环。whlie循环通过一个能够产生或转bool值的
# 表达式控制循环，表达式的值是True循环继续，表达式的值为False循环结束。

"""
猜数字游戏
计算机出一个1~100之间的随机数由人来猜
计算机根据人猜的数字分别给出提示大一点/小一点/猜对了
"""
# import random
# answer = random.randint(1, 100)
# counter = 0
# while True:
# 	counter += 1
# 	number = int(input('请输入您猜选的数字：'))
# 	if number < answer:
# 		print('再猜大一点')
# 	elif number > answer:
# 		print('再猜小一点')
# 	else:
# 		print('恭喜您猜对了！')
# 		break
# print('你一共猜了%d次' %counter)
# if counter > 7:
# 	print('你的智商有点略低。。。')

# break关键字来提前终止循环，需要注意的是break只能终止塔所在的那个循环，
# 这一点是使用嵌套的循环结构需要引起注意，除了break,还有另一个关键字continus,它可以用来
# 放弃本次循环后续的代码直接让循环进入下一轮

"""
九九乘法表输出
"""
print('-----------------九九乘法口诀表-----------------')
for i in range(1, 10):
	lineStr = ''
	for j in range(1, i + 1):
		# lineStr += str(j) + '*' + str(i) + ' = ' + str(i * j) + '\t   '
		print('%d*%d=%d' %(j, i, j * i), end='\t')
	# print(lineStr, '\r')
	print()


