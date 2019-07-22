# 匿名函数
# 当传入函数时，有些时候，不需要显示地定义函数，直接传入匿名函数更方便
l = list(map(lambda x: x * x, [1, 2, 3, 4, 5]));
print(l);
# lambda x: x * x 实际上就是匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数
# 匿名函数有个限制，只能有一个表达式，不用写return，返回值就是该表达式的结果
# 匿名函数有个好处，因为没有函数名字，不必担心函数名冲突。
# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x;
print(f(5));

# 也可以把匿名函数作为返回值返回
def build(x, y):
	return lambda: x * x + y * y;
print(build(1, 3)());

fr = filter(lambda x: x % 2 == 1, range(1, 10));
print(list(fr));











