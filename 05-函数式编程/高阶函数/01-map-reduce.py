# Python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数一次作用到序列的每个元素，
# 并把结果作为新的Iterator返回
def f(x):
	return x * x;
r = map(f, range(1, 10));
print(list(r));

s = map(str, range(1, 10));
print(list(s));