# Python的循环有两种，一种是for...in循环，依次把list或tuple中的每一个元素迭代出来
names = ['后裔', '黄忠', '虞姬', '伽罗', '孙尚香'];
for name in names:
	print(name)
# for x in ... 循环就是把每一个元素代入变量x，然后执行缩进块的语句
# 再比如我们想计算1-10的整数之和，可以用一个sum变量做累加：
sum = 0;
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	sum += x;
print('1-10的总和是：%d'%sum);

# 如果要计算1-100的整数之和，从1写到100有点困难
# Python提供一个range()函数，可以生成一个整数序列，在通过list()函数可以转换为list
# 如range(5)生成的序列是从0开始小于5的整数
# 计算1-100的整数和
sum2 = 0;
for n in list(range(101)):
	sum2 += n;
print('1-100之间的所有数的和是：%d'%sum2);


# 第二种循环是while循环，只要条件满足就不断循环，条件不满足时就退出循环
# 例如计算100一杯所有奇数之和
sum3 = 0;
m = 99;
while (m > 0):
	sum3 += m;
	m -= 2;
print('100以内所有奇数之和是%d'%sum3)

# break
# 在循环中, break语句可以提前退出循环，
# continue
# 在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。