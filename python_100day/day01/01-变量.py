"""
使用变量保存数据并进行算术运算
"""
a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

"""
使用input()函数获取键盘输入
使用int()进行类型转换
用占位符格式化输出的字符串
"""
c = int(input('c = '))
d = int(input('d = '))
print('%d + %d = %d' %(c, d, c +d))


"""
使用type()检查变量的类型
"""
e = 'Hello World!'
print(type(e))

"""
在对变量类型进行转换时可以使用Python的内置函数（准确的说下面列出的并不是真正意义上的函数，
而是后面我们要讲到的创建对象的构造方法）
"""
# int() 将一个数值或字符串转换成整数，可以指定进制
# float() 将一个字符串转换成浮点数
# str() 将指定的对象转换成字符串形式，可以指定编码
# chr() 将整数转换成该编码对应的字符串（一个字符）
# ord() 将字符串（一个字符）转换成对应的编码（整数）


# 运算符
# Python支持多种运算符
# [] [:] 下标，切片
# ** 指数
# ~ + - 按位取反，正负号
# * / % // 乘 除 模 整除
# + - 加 减
# >> << 右移 左移
# & 按位与
# ^ | 按位异或 按位或
# <= < > >=  小于等于 小于 大于 大于等于
# == !=  等于 不等于
# is is not 身份运算符
# in not in 成员运算符
# not or and 逻辑运算符
# 在实际的开发中，如果搞不清楚运算符的优先级，可以使用括号来确运算符的执行顺序

import math
radius = float(input('请输入圆的半径：'))
around = 2 * math.pi * radius
area = math.pi * radius * radius
print('圆的周长是：%.2f' % around)
print('圆的面积是：%.2f' % area)

# 判断是不是闰年
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
			year % 400 == 0)
print(is_leap)

