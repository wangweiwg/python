# 获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型，有哪些方法呢？


# 使用type(), 判断对象类型，基本类型都可以用type()判断
type(1234)
type('1234')
type(list())

def test_type():
	pass
print(type(test_type))

class Student(object):
	pass
s = Student()
print(type(s))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么处理？可以使用types模块中定义的常量：
import types
def fn():
	pass

print(type(fn)) # <class 'function'>
print(types.FunctionType) # <class 'function'>
print(type(fn) == types.FunctionType) #True

# 对于class的继承关系来说，使用type()很不方便，要判断class的类型，可以使用isinstance()函数
class Animal(object):
	pass

class Dog(Animal):
	pass

dog = Dog()
isinstance(dog, Dog)
isinstance(dog, Animal)
# isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上

# 能用type()判断的基本类型也可以用isinstance()判断
isinstance('123', str)
isinstance(123, int)

# 还可以判断某一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple
isinstance('123', (list, str))

# 总是优先使用isinstance()判断类型，可以将指定类型及其子类‘一网打尽’


# 如果要获得一个对象的所有属相和方法，可以使用dir()函数，它返回一个包含字符串的list
# 比如获得一个str对象的所有属性和方法：
print(dir('ABC'))
print('ABC'.__len__())


# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图
# 获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__方法，所以，下面两行代码是等价的：
len('abc')
'abc'.__len__()


# 当自己定义的类，想使用len()的话，需要自己写一个__len__方法
class MyClass(object):
	def __len__(self):
		return 100

# 测试
myClass = MyClass()
print(len(myClass)) # 100


# 配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态
class MyObject(object):
	def __init__(self):
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()
# 判断是否有属性 x
hasattr(obj, 'x') # True
# 获取属性 x
getattr(obj, 'x') # 9
# 判断是否有属性 y
hasattr(obj, 'y') # False
# 设置属性 y 为 10
setattr(obj, 'y', 10) 
# 判断是都有属性 y
hasattr(obj, 'y') # True
# 获取属性 y
getattr(obj, 'y') # 10

# 如果试图获取不存在的属性，就会获得AttributeError:的错误
# 可以传入一个default参数，如果属性不存在，就返回默认的值
getattr(obj, 'notIn', 404) # 404

# 是否存在方法
hasattr(obj, 'power') # True
# 获得对象的方法
getattr(obj, 'power') # 得到power函数


