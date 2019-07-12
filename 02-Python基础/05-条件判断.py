# 条件判断
# elif 是 else if 的缩写，完全可以有多个elif
# if语句执行有个特点，它是从上往下判断，如果再某一个判断上是True,把该判断对应的语句执行后，
# 就忽略掉剩下的elif和else
age = 6;
if age >= 10:
	print('your age is %d, you are teenager' % age);
elif age >= 18:
	print('your age is %d, you are adult' %age);
else:
	print('your age is %d, you are child' %age);

# 看一下例子
birth = int(input('please input your birth:'));
if birth < 2000:
	print('生于00前');
else:
	print('生于00后');
# 这样的话会报错，因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换为整数
# Python提供了int()函数来完成

# 练习题
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
print('请检测一下自己的BMI');
weight = float(input('请输入体重：'));
height = float(input('请输入身高：'));
bmi = weight / height / height;
if bmi < 18.5:
	print('BMI是---%.2f--过轻'%bmi);
elif bmi >= 18.5 and bmi < 25:
	print('BMI是---%.2f--正常'%bmi);
elif bmi >= 25 and bmi < 28:
	print('BMI是---%.2f--过重'%bmi);
elif bmi >= 28 and bmi < 32:
	print('BMI是---%.2f--肥胖'%bmi);
else:
	print('BMI是---%.2f--严重肥胖'%bmi);