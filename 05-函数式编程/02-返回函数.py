# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 实现一个可变参数的求和：
def calc_sum(*args):
	sum = 0;
	for n in args:
		sum += n;
	return sum;
# 但是，如果不需要立即求和，而是在后面的代码中，根据需要计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
	def sum():
		sum = 0;
		for n in args:
			sum += n;
		return sum;
	return sum;
# 当调用lazy_sum()时，返回的并不是求和结果，而是求和函数
f5 = lazy_sum(1, 2, 3, 4, 5);
print(f5);
# <function lazy_sum.<locals>.sum at 0x000001651BB43378>
# 在函数lazy_sum中又定义了一个函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回
# 函数sum时，相关参数和变量都保存在返回的函数中，这种称为‘闭包’的程序结构拥有极强的威力。
# 当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数


# 闭包
# 注意返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数应用
# 返回的函数并没有立即执行
def count():
	fs = [];
	for n in range(1, 4):
		def ft():
			t = n * n;
			return t;
		fs.append(ft);
	return fs;
c = count();
for fc in c:
	print(fc());
# c中每一个函数执行的结果都是9，原因就在于返回的函数引用了变量i，但它并非立即执行，等到3个函数都返回时，
# 它们所引用的变量i已经变成了3，因此最终结果为9
# 返回闭包时要牢记一点，返回函数 不要引用任何循环变量，或者后续会发生变化的变量
# 如果一定要引用，再创建一函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count2():
	fs = [];
	for n in range(1, 4):
		def ft2():
			return n * n;
		fs.append(ft2());
	return fs;
c1 = count2();
print(c1[0]);
print(c1[1]);
print(c1[2]);




