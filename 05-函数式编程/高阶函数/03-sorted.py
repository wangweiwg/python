# 排序算法
# Python内置的sorted()函数就可以对list进行排序：
print(sorted([12, 3, 67, -13, 78]));

# 还可以接受一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([12, 3, 67, -13, 78], key=abs));
# key指定的函数将作用于list的每一个元素，并根据key函数返回的结果进行排序，
# 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素
# 字符串比较时是按照ASCII的大小比较的。
# 忽略大小写排序，实际上即时先把字符串都变成大写活小写，再比较：
# 给sorted传入key函数，即可实现忽略大小写的排序：
print(sorted(['bob', 'about', 'Zoo', 'Credit']));
# ['Credit', 'Zoo', 'about', 'bob']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower));
# ['about', 'bob', 'Credit', 'Zoo']

# 如果要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True));
# ['Zoo', 'Credit', 'bob', 'about']

# 练习
# 假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)];
def by_tuple_name(t):
	return t[0];
def by_name(l):
   	return sorted(L, key=by_tuple_name);
L2 = by_name(L);
print(L2);