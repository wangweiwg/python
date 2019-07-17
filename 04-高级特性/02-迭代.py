# 迭代
# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代(Iteration)
# 在Python中，迭代是通过for...in来完成的
list = [1, 2, 3, 4, 5];
for n in list:
	print(n);
# Python的for循环不仅可以用在list或tuple上，还可以作用在其它可迭代对象上。但是，只要是可迭代对象，
# 无论有无下标,都可以迭代,比如dict就可以迭代
dict = {'a': 1, 'b': 2, 'c': 3};
for key in dict:
	print(key);
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in dict.values(),
# 如果要同时迭代key和value，可以用for k, v in dict.items()
# 由于字符串也是可迭代对象，因此，也可以用于for循环
for ch in 'ABC':
	print(ch);

# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该
# 对象究竟是list还是其他数据类型。
# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable;
print('字符串：', isinstance('abc', Iterable));
print('list：', isinstance([1, 2, 3], Iterable));
print('数字：', isinstance(123, Iterable));

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
for i, value in enumerate(['A', 'B', 'C', 'D', 'E']):
	print(i, value);


# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
	minX = L[0];
	maxX = L[0];
	if L == []:
		return (None, None);
	else:
		for item in L:
			if item < minX:
				minX = item;
			if item > maxX:
				maxX = item;
		return (minX, maxX);
r = findMinAndMax([3, 9, 4, 19, 1, 8]);
print(r);


