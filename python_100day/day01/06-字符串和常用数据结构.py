str1 = 'hello, world!'
# 计算字符串的长度
print(len(str1))
# 首字母大写
print(str1.capitalize())
# 字符串变大写
print(str1.upper())
# 查找子串所在位置
print(str1.find('llo')) # 找不到时返回-1
print(str1.index('llo')) # 找不到时会出现异常
# 查找字符串是否以指定的字符串开头
print(str1.startswith('hell'))
# 查找字符串是否以指定的字符串结尾
print(str1.endswith('orld!'))
# 将字符串以指定的宽度居中并在两侧填充指定的字符串
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符串
print(str1.rjust(50, '-'))
print(str1.ljust(50, '#'))

str2 = 'abcdefg'
# 从指定的开始索引到指定的结束索引
print(str2[2])
print(str2[2:5]) # 不包含第5位
print(str2[2:])
print(str2[2::3]) # 3代表步长
print(str2[::2])
print(str2[::-1]) # 倒着排列
print(str2[-3:-1]) # 不包含最后一位

# 字符串是否由数字构成
print(str2.isdigit()) # False
# 字符串是否以字母组成
print(str2.isalpha()) # True
# 字符串是否以数字和字母构成
print(str2.isalnum()) # True

str3 = '     avbn@163.com'
# 字符串去除空格
print(str3)
print(str3.strip())


# Python内置了很多类型的数据结构，除了字符串包括列表、元组、集合和字典
# 使用列表：
list1 = [1, 2, 3, 4, 5]
list2 = ['hello'] * 5
print(list1)
print(list2)
# 计算列表的长度
print(len(list1))
# 根据下标取元素
print(list1[2])
list1[3] = 30
print(list1[3])
# 添加元素
list1.append(500)
list1.insert(1, 100)
# 删除元素
list1.remove(1) # 删除元素1
if 500 in list1:
	list1.remove(500) 

# 删除下标为0的元素
del list1[0]
# 清空列表元素
list1.clear()
print(list1)


# 和字符串一样，列表也可以做切片操作，
fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 循环遍历列表元素
for fruit in fruits:
	print(fruit.title(), end=' ')
print()

# 列表切割
fruits2 = fruits[1:4]
print(fruits2)

# fruits3 = fruits # 没有哦复制列表只创建了新的引用
# 可以通过完整切片操作来复制列表
fruits3 = fruits[:]
fruits4 = fruits[-3:-1]
print(fruits4)
# 可以通过反向切片操作来获得倒转后的列表的拷贝
fruits5 = fruits[::-1]
print(fruits5)

# 对列表的排序操作
# sorted函数返回列表排序后的拷贝不会修改传入的列表
fruits6 = sorted(fruits)
print(fruits6)
fruits7 = sorted(fruits, reverse=True)
print(fruits7)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
fruits8 = sorted(fruits, key=len)
print(fruits8)

# 利用列表的生成式语法来创建列表，代码如下所示：
import sys
list3 = [x for x in range(5)]
print(list3)
list4 = [x + y for x in 'ABCDE' for y in '123456789']
print(list4)

# 用列表的生成表达式语法创建列表容器
# 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
list5 = [x ** 2 for x in range(1, 100)]
# 查看对象占用的内存的字节数
print(sys.getsizeof(list5))
print(list5)











