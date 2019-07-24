# 继承和多态
# 在OOP程序设计中，当定义一个class的时候，可以从某一个现有的class继承，新的class称为子类(Subclass)，而被继承的class
# 称为基类、父类或超类(Base class、Super class)
# 例如：已经编写一个Animal的class，有一个run()方法可以直接打印：
class Animal(object):
	def run(self):
		print('Animal is running ...')

# 当我们需要Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
	pass

class Cat(Animal):
	def run(self):
		print('Cat is running ...')

# 对于Dog来说，Animal就是他的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似
# 继承最大的好处是子类获得了父类的全部功能。由于Animal实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，
# 就自动拥有了run()方法
dog = Dog()
dog.run();

cat = Cat()
cat.run()

# 也可以对子类增加一些方法，比如Dog类
class Dog1(Animal):
	def run(self):
		print('Dog is running ...')

	def eat(self):
		print('Dog is eating meat ...')
dog1 = Dog1()
dog1.run() # 调用的是子类自身的run方法
dog1.eat()
# 继承第二个好处需要我们对代码做一点改进，无论是Dog还是Cat，它们调run()的时候，需要打印自身的信息，
# 这时候需要重写父类的run()方法
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行时，总是会调用子类
# 的run()。这样我们就获得了继承的另一个好处：多态

# 要理解什么是多态，首先对数据类型做一点说明，当我们定义一个class的时候，实际上就定义了一种数据类型。我们定义的数据类型
# 和Python自带的数据类型，比如str、list、dict没有什么区别:
a = list()
print(isinstance(a, list)) # True
print(isinstance(dog1, Dog1)) # True
print(isinstance(dog1, Animal)) # True
# dog1不仅仅是Dog，还是Animal
# 在继承关系中，如果一个实例的数据类型是某一个子类，那它的数据类型也可以被看做是父类，但是，反过来就不行
# Dog可以看成Animal，但是Animal不可以看成Dog


# 为了更好地理解多态，再定义一个接收Animal变量类型的函数
def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())
# 传入一个实例时，打印两次Animal is running

# 当传入Dog的实例时，run_twice()就打印两次 Dog is running
run_twice(dog1)

# 当传入Cat实例时，run_twice()就打印两次 Cat is running
run_twice(cat);


# 如果再定义一个Tortoise类型，也从Animal派生
class Tortoise(Animal):
	def run(self):
		print('Tortoise is running ...');

# 再次调用run_twice()函数，传入tortoise实例，打印两次 Tortoise is running ...
run_twice(Tortoise())

# 这时候发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的
# 函数或者方法都可以不加修改地正常运行，原因就在于多态


# 堕胎的好处就是，当我们需要传入Dog、Cat、Tortoise ...时，我们只需要接收Animal类型就可以了，因为Dog、Cat、
# Tortoise ...都是Animal类型，然后，按照Animal类型操作就可以了。由于Animal类型有run()方法,因此，传入任意
# 类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思

# 对于一个变量，我们只需要知道它是Animal类型，无需确切的知道它的子类型，就可以放心地调用run()方法，而具体调
# 用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时改对象的确切类型决定，这就是多态真正的威
# 力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码
# 是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数
# 继承还可以一级一级的继承下来，就好比爷爷到爸爸，再到儿子这样的关系，而任何类，最终都可以追溯到根类object，
# 这些继承关系看上去就像一颗倒着的树，


# 静态语言 VS 动态语言
# 对于静态语言(例如Java)来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，
# 将无法调用run()方法
# 对于Pyhthon这样的动态语言来说，则不一定需要传入Animal类型，我们只要保证传入的对象有一个run()方法就可以了
class Timer(object):
	def run(self):
		print('Start timer ...')
run_twice(Timer())
# 这就是动态语言‘鸭子类型’，它并不要求严格的继承体系，一个对象只要‘看起来像鸭子，走起路来像鸭子’，
# 那它就可以被看做鸭子
# Python的‘file-like object’就是一种鸭子类型，对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，
# 只要有read()方法，都被视为‘file-like object’。许多函数接收的参数就是‘file-like object’，你不一定要传入真正的
# 文件对象，完全可以传入任何实现了read()方法的对象