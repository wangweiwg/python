# 类和实例
# 面向对象最重要的概念就是类(Class)和实例(Instance)，必须牢记类是抽象的模板，比如Student类，
# 而实例是根据类创建出来的一个个具体的‘对象’，每个对象都拥有相同的方法，但各自的数据可能不同
# Python中，定义类是通过class关键字：
class Student(object):
	pass
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object),表示该类是
# 从哪个类继承下来的，继承的概念后边讲，通常没有合适的继承类，就使用object类，这是所有类最终
# 都会继承的类
# 定义好Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现
xiaoming = Student()
# 可以给实例自由的绑定一个属性，比如name属性：
xiaoming.name = '小明'

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强
# 强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属
# 性绑上去。

class Student1(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
# 注意__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
# 就可以把各种属性绑定到self，因为self就指向创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了。必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去：
xiaoqiang = Student1('小强', 95)
print(xiaoqiang.name)
print(xiaoqiang.score)
# 和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，
# 调用时，不用传递该参数。除此之外，类的方法和普通函数没有区别，所以，仍然可以用默认参数、
# 可变参数和命名关键字参数


# 数据封装
# 面向对象编程的一个重要特点就是数据封装。上面Student1类中，每一个实例就拥有各自的name和score，
# 可以通过实例访问这些数据，也可以通过函数输出：
def print_student_info(student):
	print('姓名：%s---分数：%s' %(student.name, student.score));
print_student_info(xiaoqiang);

# 但是，既然Student1实例本身就拥有这些数据，要访问这些数据，就没必要通过print_student_info来访问，
# 可以直接在Student1类的内部定义访问数据的函数，这样，就把‘数据’封装起来了，这些封装数据的函数是和
# Student1类本身是关联起来的，我们称之为类的方法：
class Student3(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	
	def print_student_info(self):
		print('姓名：%s----分数：%s' %(self.name, self.score))

	def print_score(self):
		print('成绩是：%s' %self.score);

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 75:
			return 'B'
		elif self.score >= 60:
			return 'C'
		else:
			return 'D'

# 创建实例
xiaowang = Student3('小王', 90)
xiaowang.print_student_info()
xiaowang.print_score()

# 要定义一个方法，除了第一个参数是self外，其他都和普通函数一样，要调用一个方法，只需要再实例变量上直接调用，
# 除了self不用传递，其他参数正常传入
# 这样，我们从外部看Student3类，就只需要知道，创建实例需要给出name和score，而何时打印，都是在Student3类的
# 内部定义的，这些数据和逻辑被‘封装’起来了，调用很容易，但却不知道内部实现的细节。
# 封装的另一个好处是可以给Student3类增加新的方法，比如get_grade
# 同样get_grade方法可以直接在实例变量上调用，不需要知道内部实现细节
grade_type = xiaowang.get_grade()
print(grade_type) # A