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