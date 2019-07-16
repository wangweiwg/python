# 定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道如何传递正确的参数，
# 以及函数将返回什么样的值就够了，函数内部的复杂逻辑被封装起来，调用者无需了解
# Python的函数定义非常简单，灵活度非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义
# 出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
# 计算x的平方的函数：
def power(x):
	return x * x;

# 要计算三次方、四次方、n次方
def powern(x, n = 2):
	r = 1;
	while n > 0:
		n -= 1;
		r = r * x;
	return r;
# 测试 5的立方
print(powern(2, 5));
print(powern(2))
# 默认参数2，计算平方
# 设置默认参数有几点需要注意：
# 1、必选参数在前，默认参数在后，否则Python的解释器会报错
# 2、如何设置默认参数，当参数有多个时，把变化大的参数放前面。变化小的参数就可以作为默认参数
# 3、使用默认参数的好处是降低调用参数的难度。
# 4、如果有多个默认参数，既可以按照顺序传递一一对应的，也可以不按照顺序，当不按顺序传递时需要把参数名写上
def person(name, age, gender = '男', city = '北京'):
	print('name = %s age = %s gender = %s city = %s' %(name, age, gender, city));
xiaoming = person('小名', 20);
xiaoqing = person('小青', 22, '女', '河北');
xiaohong = person('小红', 25, city = '青岛');

# 如果默认参数是一个list，并且list默认为[], 调用的时候会出问题
def add_list(list = []):
	list.append('测试');
	return list;
print(add_list());
print(add_list());
print(add_list());
# ['测试', '测试', '测试']
print(add_list([1, 2, 3]));
# [1, 2, 3, '测试']
# Python函数在定义的时候，默认参数list的值就被计算出来了，即[], 因为默认参数list也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了list的内容，则下次调用时默认参数的内容就变了，不再是函数定义时的[]了。
# 注意：定义默认参数要牢记一点：默认参数必须指向不变对象！！！
# 修改上面的函数，要用None这个不变对象来实现：
import math;
def add_list2(list2 = None):
	print(list2 is None)
	if list2 is None:
		list2 = [];
	list2.append('测试');
	return list2;
print(add_list2());
print(add_list2());
print(add_list2());


# 可变参数：
# 例如：给定一组数a、b、c...，请计算它们的平方和
def calc(numbers):
	sum = 0;
	for n in numbers:
		sum += math.pow(n, 2);
	return sum;
print(calc([1, 2, 3, 4]));

# 把函数参数变成可变参数
def calc2(*numbers):
	sum = 0;
	for n in numbers:
		sum += math.pow(n, 2);
	return sum;
print(calc2(1, 2, 3, 4));
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号，参数numbers接收到的是一个tuple，在调用的时候
# 可以传入任意个参数，包括0个参数
# 有时候我们已知固定的list 或者tuple，但是函数的参数是可变的，这时候可以把list或tuple转化为可变的参数传入函数
# 只需要在传参的时候在前面加*号就可以了
nums = [1, 2, 3, 4];
calc2(*nums);
# *nums表示把这个list的所有元素作为可变参数传进去



# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含
# 参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def car(brand, color, **kw):
	print('brand:', brand, 'color:', color, 'remarks:', kw);
# 调用car
car('奔驰', '黑色');
car('奔驰', '黑色', test = '测试关键字参数');
car('奥迪', '红色', seats = '7座', type = '自动挡');
# 关键字参数有什么用处呢？它可以扩展函数的功能。例如，在car函数里面，我们保证能收到brand、color这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。假如做一个注册功能，除了用户名和年龄是必填项外，其它都
# 是选填项，利用关键字参数来定义这个函数就能满足注册的需求。
# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去。
extra = {'seats': '5座', 'type': '自动挡'};
car('宝马', '蓝色', **extra);
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得
# 的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra


# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查
# 仍以car函数为例，我们希望检查是否有seats和type参数：
def car2(brand, color, **kw):
	if 'seats' in kw:
		pass;
	if 'type' in kw:
		pass;
	print('brand:', brand, 'color:', color, 'remarks:', kw);
# 这样的话调用者仍然可以传入不受限制的关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如：只接受seats和type作为关键字参数定义方式如下：
def car3(brand, color, *, seats, type):
	print(brand, color, seats, type);
car3('劳斯莱斯', '黑色', seats = '8座', type = '全自动');
# 和关键字参数**kw不同，命名关键字参数需要一个特殊的分隔符*， *后面的参数被视为命名关键字参数
# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了；
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符，如果缺少*，Python解释器
# 将无法识别位置参数和命令关键字参数：
def car4(brand, color, *args, seats, type):
	print(brand, color, args, seats, type);
# 命名关键字参数必须传入参数名，这和位置参数不同，如果没有传入参数名，调用将报错：
# 命名关键字参数，也可以是含有默认值的参数。



# 参数组合
# 自定义函数时，可以使用必须参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用，
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 例如：
def fun1(a, b, c = 0, *args, **kw, ):
	print('a = ', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw);

def fun2(a, b, c = 0, *, d, **kw):
	print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw);

fun1(1, 2, 3, 4, 5, key = 1, value = 2);
fun2(1, 2, 3, d = 4, key = 1, value = 2);

# 奇怪的是通过一个tuple和dict，也可以调用fun1
args = (1, 2, 3, 4, 5);
kw = {'key': 1, 'value': 2};
fun1(*args, **kw);
# 对于任意函数，都可以通过类似fun(*args, **kw)的形式调用它，无论它的参数是如何定义的
# 虽然可以组合多达5种参数，但不要同时使用太多的组合，否则函数接口的理解性很差。


# 练习
# 以下函数允许计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*nums):
	p = 1;
	for x in nums:
		p = p * x;
	return p;
rel = product(1, 2, 3, 4, 5);
print('乘积是：', rel);


