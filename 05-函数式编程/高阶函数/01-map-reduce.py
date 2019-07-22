# Python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数一次作用到序列的每个元素，
# 并把结果作为新的Iterator返回
def f(x):
	return x * x;
r = map(f, range(1, 10));
print(list(r));

s = map(str, range(1, 10));
print(list(s));

# reduce是把一个函数作用在一个序列上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce;
def f1(x, y):
	return x * y;
reduce(f1, [1, 2, 3, 4, 5]); 
# 相当于
# f1(f1(f1(f1(1, 2), 3), 4), 5)
 # = 1 * 2 * 3 * 4 * 5;

# 例如，求一个序列的和：
from functools import reduce;
def add(x, y):
	return x + y;
sum = reduce(add, [1, 2, 3, 4, 5]);
print(sum);

# 求和的话可以使用Python内置的函数sum()，没必要使用reduce

# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0:1].upper() + name[1:].lower();

L1 = ['adam', 'LISA', 'barT'];
L2 = list(map(normalize, L1));
print(L2);
