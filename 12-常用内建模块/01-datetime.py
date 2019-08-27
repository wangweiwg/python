# datetime是Python处理日期和时间的标准库
# 获取当前日期和时间
from datetime import datetime
now = datetime.now()
print(now)
print(type(now))
# 注意datetime是模块，datetime模块还包含一个datetime类，通过 from datetime import datetime导入才是datetime这个类
# 如果仅导入import datetime, 则必须引用全名 datetime.datetime
# datetime.now() 返回当前日期和时间，类型是datetime


# 获取指定日期和时间
# 要指定某一个日期和时间，我们直接用参数构造一个datetime
dt = datetime(2019, 10, 1, 10, 10, 10)
print(dt)


# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time，
# 记为0（1970年以前的时间timestamp为负数），当前时间就是相对于epoch time的秒数，称为timestamp。
# 可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，
# 这就是为什么计算机存储的当前时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。


# 把一个datetime类型转换为timestamp只需简单调用timestamp()方法 
dt1 = datetime.now()
print(dt1.timestamp())
# 注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
 
 







