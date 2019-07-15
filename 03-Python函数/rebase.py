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
# 