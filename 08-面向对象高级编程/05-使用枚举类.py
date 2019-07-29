# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
JAN = 1
FEN = 2
# 好处是简单，缺点是类型是int，并且仍然是变量
# 更好的方法是为这样的枚举类型定义一个class类型，然后，每个常量都是calss的一个唯一实例。
# Python提供了Enum类来实现这个功能：
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就得到Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
print(Month)
for name, member in Month.__members__.items():
	print(name, '=>', member, '=>', member.value)

# value属性则是自动赋给成员的int常量，默认从1开始计数
# 如果需要精确的控制枚举类型，可以从Enum派生出自定义类：
from enum import Enum, unique

@unique
class Weekday(Enum):
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

# @unique装饰器可以帮助我们检查保证没有重复值
# 访问这些枚举类型可以有若干种方法：
day1 = Weekday.Mon
print(day1)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day1 == Weekday.Mon)
print(day1 == Weekday.Tue)
print(Weekday(1))
print(Weekday(1).value)
for name, member in Weekday.__members__.items():
	print('name -->', name, 'value-->', member.value)

# 第一种定义方法
from enum import Enum
PayType = Enum('PayType', ('Ali', 'WX'))
print('获取到的支付方式是：', PayType.Ali.value)

# 第二种定义方法
from enum import Enum, unique
@unique
class PayType1(Enum):
	Ali = 1
	WX = 2
print('获取到的第二种支付方式是：', PayType1.WX, PayType1.WX.value)
