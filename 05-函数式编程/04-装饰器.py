# 装饰器
# 函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数
def now():
	print('当前时间是2019-07-23');
f = now;
f();

# 函数对象有一个__name__属性，可以拿到函数的名字：
print(f.__name__);

# 现在，假设要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为‘装饰器(Decorator)’
# 本质上，decorator就是一个返回函数的高阶函数
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' %func.__name__);
		return func(*args, **kw);
	return wrapper;
# 因为log是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 借助Python的@语法，把decorator置于函数的定义处：
@log
def now2():
	print('2019-07-23');
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
now2();
print('now2---%s' %now2.__name__);

# 把@log放到now2()函数的定义处，相当于执行了语句
# now2 = log(now2);

# 由于log()是一个decorator，返回一个函数，所以，原来的now2()函数仍然存在，只是现在同名的now2变量指向了新的函数，
# 于是调用now2()将执行新函数，即在log()函数中返回wrapper()函数
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用
# 在wrapper()函数内，首先打印日志，再紧接着调用原始函数


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数
def console(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s--%s' %(text, func.__name__));
			return func(*args, **kw);
		return wrapper;
	return decorator;

# 使用如下：
@console('自定义log文本信息')
def now3():
	print('2019-07-23');
# 调用如下
now3();
print('三层嵌套时--', now3.__name__);
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
# now3 = log('自定义log文本信息')(now3);
# 首先执行log('自定义log文本信息')，返回的是decorator函数，再调用返回的函数，参数是now3函数，
# 返回最终是wrapper函数
# 可以发现，经过decorator装饰之后的函数，他们的__name__已经从原来的'now3'变成了'wrapper',因为返回的
# 那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，
# 有些依赖函数的签名的代码执行就会出错
# Python内置的functools.wraps就是干这个事的
# 完整的decorator的写法如下：
import functools;
def logNew(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s' %func.__name__);
		return func(*args, **kw);
	return wrapper;

# 带参数的同样在定义wrapper函数的前面加上 @functools.wrap(func)即可
# import functools是导入functools模块






