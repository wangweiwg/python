# 访问限制
# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑
# 但是从Student类的定义来看，外部代码还是可以自由的修改一个实例的name、score属性

# 如果让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了
# 一个私有变量(private)，只有内部可以访问，外部不能访问，例如：
class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def print_score(self):
		print('%s  --- %s' %(self.__name, self.__score))

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_score(self):
		return self.__score

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('score 参数不对')

# 创建一个实例
xiaoqing = Student('小青', 90)
xiaoqing.print_score()
# 外部已经无法访问实例变量__name和__score了
# print(xiaoqing.__name)
# print(xiaoqing.__score)
# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮
# 如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法
xiaoqing.get_name()
xiaoqing.get_score()

# 如果允许外部代码修改name和score，可以给Student类增加set_name和set_score方法：
xiaoqing.set_name('小青青')
xiaoqing.set_score(78)
xiaoqing.print_score()

# 令人迷惑的是，之前那种直接通过xiaoqing.name也可以修改，为什么要定义方法呢？因为在方法中，可以对参数做检查，
# 避免传入无效的参数
# set_score对参数进行检查，判断是否在0--100之间
# xiaoqing.set_score(120)

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名
# 有时候会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成
# 的规定，当看到这样的变量时，意思就是，虽然我可以被访问，但是，请把我视为私有变量，不要随意访问

# 双下划线开头的变量是不是一定不能从外部访问？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量
# 改成了_Student__name，所以可以通过_Student__name来访问__name变量
print('通过_Student__name访问__name是：', xiaoqing._Student__name)

# 但是强烈建议不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名

# 问题:
xiaoshuai = Student('小帅', 80)
xiaoshuai.__name = '大帅'
print(xiaoshuai.__name)
xiaoshuai.print_score()
# 表面上看可以设置__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量。内部的__name变量已经被Python
# 解释器自动改成了_Student_name，而外部代码给xiaoshuai新增了一个__name变量