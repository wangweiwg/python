# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
	print('2019-07-22');
f = now;
f();
# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__);

# 现在要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为’装饰器(Decorator)‘。

def log(func):
	def wrapper(*args, **kw):
		print('调用了函数 %s()' %func.__name__);
		return func(*args, **kw);
	return wrapper;
# 观察log函数，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数，
# 借助Python的@语法，把decorator置于函数的定义处
@log
def now1():
	print('当前时间是2019-07-22');
now1();

# 把@log放到now()函数的定义处，相当于执行了语句:
# now1 = log(now1);
# 由于log()是一个decorator，返回一个函数，所以，原来的now1()函数仍然存在，只是现在同名的now1变量
# 指向了新的函数，于是调用now1()将执行新函数，即在log()函数中返回的wrapper()函数。
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，



