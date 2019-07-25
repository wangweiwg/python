# 实例属性和类属性
# 由于Pyhthon是动态语言，根据类创建的实例可以任意绑定属性
# 给实例绑定属性的方法是通过实例变量，或者通过self变量
class Student(object):
	def __init__(self, name):
		self.name = name

s = Student('小强')
s.score = 90

# 但是，如果Student类本身需要绑定一个属性呢？可以直接在calss中定义属性，这种属性是类属性，归Student类所有：
class Student2(object):
	name = 'Student'
# 定义一个类属性name，这个属性虽然归类所有，但类的所有实例都可以访问到
s2 = Student2()
print(s2.name) # Student， 因为实例并没有name属性，所有会继续查找class的name属性
print(Student2.name) # Student，打印类的name属性
s2.name = '实例的nam属性'
print(s2.name) # 实例的nam属性，由于实例属性优先级比类属性高，因此它会屏蔽掉类的name属性，但是类的name属性并没有消失

# 删除实例的属性
del s2.name
print(s2.name) # Student, 由于实例的属性没了，这时候会查找到类的属性

# 因此，在编程的时候，不要对实例属性和类属性使用相同的名字，因为，相同名称的实例属性将屏蔽掉类属性，
# 但是当删除实例属性后，再使用相同的名称，访问到的将是类属性



