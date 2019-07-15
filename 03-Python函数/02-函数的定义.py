# 在Python中定义一个函数要用def语句，
# 依次写出函数名、括号、括号中的参数和冒号:，然后在缩进块中编写函数体，函数的返回值用return语句返回


# 定义一个求绝对值的函数：
def my_abs(x):
	if x > 0:
		return x;
	else:
		return -x;
# 调用my_abs函数
a = my_abs(-120);
print(a);
# 注意：函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并将结果返回。因此函数内部通过
# 条件判断和循环可以实现非常复杂的逻辑
# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None，return None可以简写为return。
# 在Python交互环境中定义函数时，注意Python会出现...的提示，函数定义结束后需要按两次回车重新回到>>>提示符下：

# import 语法
# from * import *


# 空函数：
# 如果想定义一个空函数，可以用pass语句
def nop():
	pass;
# pass语句什么都不做，实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放
# 一个pass，让代码先能运行起来
# pass还可以用在其他语句里：
age = 19;
if age > 18:
	pass;
# 缺少了pass，代码运行就会有语法错误

# 当传入不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的函数my_abs没有参数检查
# 修改my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。
# 数据类型检查可以用内置函数isinstance()实现
def my_abs2(x):
	if not isinstance(x, (int, float)):
		raise TypeError('参数类型错误');
	if x >= 0:
		return x;
	else:
		return -x;
print(my_abs2(-1234));

# 返回多个值
# 导入math包，并允许后续代码应用math包里的sin、cos等函数
import math;
def move(x, y, step, angle = 0):
	nx = x + step * math.cos(angle);
	nx = y - step * math.sin(angle);
	return nx, ny;
# Python函数返回的仍然是单一值：
# 返回值是一个tuple，返回一个tuple可以省略括号


# 练习
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2 + bx + c = 0 的两个解。
def quadratic(a, b, c):
	x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a;
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a;
	return x1, x2;
result = quadratic(1, -6, 9);
print(result);


