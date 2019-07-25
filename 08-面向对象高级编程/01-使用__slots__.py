# 当定义一个calss，创建一个class实例后，可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class
class Student(object):
	pass

# 创建实例
s = Student()
# 给实例动态绑定一个属性：
s.name = '小强'
print(s.name)

# 还可以给实例绑定一个方法：
# 定义一个函数作为实例的方法
def set_age(self, age):
	self.age = age
	print('%s的年龄是：%s' %(self.name, self.age))
def set_score(self, score):
	self.score = score
	print('%s的分数是：%s' %(self.name, self.score))

from types import MethodType
# 给实例绑定方法
s.set_age = MethodType(set_age, s)
# 使用
s.set_age(20)
print('%s的年龄是%s' %(s.name, s.age))

# 但是给一个实例绑定的方法，对另一个实例是不起作用的：
# 创建实例s1
s1 = Student()
s1.name = '小张'
# s1.set_age(28) # 报错， has no attribute set_age


# 为了给所有实例绑定方法，可以给class绑定方法：
Student.set_score = set_score
s.set_score(70)
s1.set_score(80)

# 通常情况下，set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，
# 这在静态语言中很难实现


# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如只允许Studen实例添加name和age属性，而不能添加其它的属性
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Student3(object):
	# 使用tuple定义允许绑定的属性名称
	__slots__ = ('name', 'age')

# 创建实例
s3 = Student3()
s3.name = '小红'
s3.age = 18
print('我的名字叫%s，我今年%s了' %(s3.name, s3.age))
# s3.score = 80 
# 由于score没有被放到__slots__中, 所以不能绑定score属性。报错， has no attribute score


# 使用__slots__要注意，__slots__定义的属性仅对当前实例起作用，对继承的子类是不起作用的：
class MiddleStuden(Student3):
	__slots__ = ('score', 'height')

# 创建实例
middleStudent = MiddleStuden()
middleStudent.score = 97
print(middleStudent.score)

middleStudent.name = '我是中学生'

# 报错
# middleStudent.weight = '60Kg'

# 在子类中也定义__slots__，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__



