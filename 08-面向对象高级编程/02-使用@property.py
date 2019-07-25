# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是没办法检查参数，导致可以把成绩随便修改：
class Student(object):
	pass

s = Student()
s.score = 900

# 显然有点不合理，可以通过set_score()方法设置成绩，再通过get_score()获取成绩，在set_score()方法里做检查参数
class Student2(object):
	def get_score(self):
		return self.score

	def set_score(self, value):
		if not isinstance(value, int):
			raise ValueError('参数类型不正确')
		if value < 0 or value > 100:
			raise ValueError('参数在0 ~~ 100之间')
		self.score = value

s2 = Student2()
s2.set_score(78)
s2.get_score()


# 这样使用set_score和get_score的方法有点复杂，
# 还记得装饰器(decorator)可以给函数动态添加功能吗？对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student3(object):
	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('参数类型不正确，应该为 int 类型')
		if value < 0 or value > 100:
			raise ValueErro('参数范围为 0 -- 100')
		self._score = value

s3 = Student3()
s3.score = 67
s3.score

# @property的实现比较复杂，先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，就拥
# 有了一个可控的属性操作

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter
# 和setter方法来实现的。还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Person(object):
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self, value):
		self._birth = value

	@property
	def age(self):
		return 2019 - self._birth

p = Person()
p.birth = 1991
print('p的年龄是：%s' %p.age)
	
	






