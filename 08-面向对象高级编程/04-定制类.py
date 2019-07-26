# 定制类：
# 看到类似__slots__这种形如__xxx__的变量或者函数名就需要注意，这些在Python中都是有特殊用途的
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数
# 除此之外，Python的class中还有许多这样特殊用途的函数，可以帮助我们定制类。


# __str__
# 定义一个Student类，打印一个实例
class Student(object):
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return 'Student object (name: %s)' %self.name

print(Student('测试'))
# <__main__.Student object at 0x00000195498EE9E8>
# 打印的不太好看，为了好看，只需要定义好__str__()方法，返回一个好看的字符串就可以了：
# 定义完__str__()方法之后：
# Student object (name: 测试)
# 这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据：
# 在Python解释去模式下，直接输入变量名，打印出来的还是不好看
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的
# 字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决的方法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个简单的写法：
class Student1(object):
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return 'Student onject (name = %)' %self.name
	__repr__ = __str__


# __iter__
# 如果一个类想被用于for ... in循环，类似list 或 tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时推出循环
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1 # 初始化两个计数器 a, b

	def __iter__(self):
		return self  # 实例本身就是迭代对象，返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100: # 退出循环的条件
			raise StopIteration()
		return self.a

	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for n in range(n):
				a, b = b, a + b
			return a
		elif isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L

for n in Fib():
	print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当做list来使用还是不行，
# 要像list那样通过下标取元素的话，需要实现__getitem__()方法
# 定义完就可以按照下标访问数列的任意一项了:
f = Fib()
print(f[0])
print(f[1])
print(f[2])
print(f[3])
# 但是list有一个神奇的切片方法：
# 对于Fib却报错，原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要判断
print(f[1:3])
print(f[0:3])

# 也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的
# 此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作为key的object，例如str
# 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值，最后，还有一个__delitem__()方法，
# 用于删除某一个元素
# 总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于
# 动态语言的“鸭子类型”，不需要强制继承某一个接口


# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错,比如定义Person类
class Person(object):
	def __init__(self):
		self.name = 'Job'

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		elif attr == 'age':
			return lambda x: x * x
		else:
			raise AttributeError('Student object has no attribute \'%s\'' % attr)

# 如果调用name属性没问题，但是如果调用不存在的score属性，就会报错：
# 要避免这分错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getatter__()，动态
# 返回一个属性，

# 当调用不存在的属性时，比如score，Python解释器会视图调用__getattr__(self, 'score')来尝试获得属性，
# 这样，我们就有机会返回score的值
p = Person()
print(p.name)
print(p.score)
# 也可以返回函数
print(p.age(5))
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
# print(p.abs)
# 此外，任何调用如p.abs都会返回None，这是因为我们定的__getattr__默认返回就是None，要让class只响应特定的
# 几个属性，我们就要按照约定，抛出AttributeError的错误

# 实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段
# 这种完全动态的调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况调用


# 举个例子：
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

# 利用完全动态的__getattr__，我们可以写出一个链式调用：
class Chain(object):
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):

		print('调用了--', path)
		return Chain('%s/%s' %(self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__


# print(Chain().status.user.timeline.list)
# /status/user/timeline/list

# 这样无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变
# 还有REST API会把参数放到URL中，比如GitHub的API
# GET /users/:user/repos
# 调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
# Chain().users('michael').repos