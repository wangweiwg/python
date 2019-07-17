# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
L = list(range(1, 11));
print(L);
# 可以使用下面的方式直接生成
L1 = [x for x in range(1, 11)];
# 还可以使用两个循环，生成全排列
L2 = [m + n for m in 'ABC' for n in 'XYZ'];
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
# 三层和三层以上的循环就很少用到了

# 运用列表生成式，列出当前目录下的所有文件和目录名：
import os;  #导入os模块
d = [d for d in os.listdir()];
print(d);

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value:
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4};
for k, v in dict.items():
	print(k, '=', v);
# 因此，列表生成式也可以使用两个变量来生成list：
L3 = [k + '=' + str(v) for k, v in dict.items()];
print(L3);

# 把一个list中所有的字符串变成小写：
L4 = ['Hello', 'World', 'I', 'AM', 'PyTHon'];
L5 = [l.lower() for l in L4];
print(L5);


# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
# 使用内建的isinstance函数可以判断一个变量是不是字符串：
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L6 = ['Hello', 'World', 18, 'I', 'AM', 'PyTHon'];
L7 = [l.lower() for l in L6 if isinstance(l, str)];
print(L7);

