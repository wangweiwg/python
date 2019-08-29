# if语句的使用
# 在Python中，要构造分支结构可以使用if、elif和else关键字，所谓关键字就是有特殊含义的单词，像if和elif就是专门用于构造
# 分支结构的关键字，很显然你不能够使用它作为变量名


"""
用户身份验证
"""
username = input('请输入用户名：')
# password = input('请输入口令：')
# 如果希望输入口令时 终端中没有回显，可以使用getpass模块的getpass函数

# 一：
# import getpass
# password = getpass.getpass('请输入口令：')

# 二：
from getpass import getpass
password = getpass('请输入口令：')

if username == 'admin' and password == '123456':
	print('身份验证成功！')
else:
	print('身份验证失败！')

# Python中没有用花括号来构造代码块而是使用了缩进的方式来设置代码的层次结构，如果if条件成立的情况下需要执行多条语句，
# 只要保持多条语句具体有相同的缩进就可以了，换句话说连续的代码如果又保持了相同的缩进那么它们属于同一个代码块，相当于
# 是一个执行的整体
# 如果要构造出更多的分支，可以使用if...elif...else结构
# 当然根据实际开发的需求，分支结构是可以嵌套的，例如判断是否通关以后还要根据你获得的宝物或者道具的数量对你的表现给出
# 等级（比如点亮两颗或三颗星星），那么我们就需要在if的内部构造出一个新的分支结构，同理elif和else中也可以再构造新的分支，
# 我们称之为嵌套的分支结构

from random import randint
num = randint(1, 6)
if num == 1:
	print('第1种')
elif num == 2:
	print('第2种')
elif num == 3:
	print('第3种')
elif num == 4:
	print('第4种')
elif num == 5:
	print('第5种')
elif num == 6:
	print('第6种')
else:
	print('其它')

# 使用了random模块的randint函数生成指定范围的随机数来模拟掷骰子
# import math
# math模块中的sqrt函数来计算平方根
# Python内置的abs()函数取绝对值




