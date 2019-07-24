# 由于Python是动态语言，根据类创建的实例可以任意绑定属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
	def __init__(self, name):
		self.name = name
s = Student('Tom')
s.score = 90

# 如果Student类本身需要绑定一个属性，可以直接在class中定义属性，这种属性是类属性，归Student类所有