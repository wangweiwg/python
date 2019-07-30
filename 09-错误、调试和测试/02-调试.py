# 程序能一次写完并正常运行的概率很小，基本不超过1%，总会有各种各样的bug需要修正，有的bug很简单，看卡错
# 误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，因此，需要
# 一套调试程序的手段来修复bug


# 第一种方法简单粗暴，就是用print()把可能有问题的变量打印出来看看
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息
# 
# 断言
# 凡是用print()来辅助 查看的地方，都可以用断言(assert)来替代
def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'
	print('n 不等于 0')
	return 10 / n

foo('0');
# assert的意思是，表达式 n != 0应该是True, 否则根据程序运行的逻辑，后面的代码肯定会出错
# n != 0 时，执行后面的程序
# n = 0 时，抛出异常AssertionError: n is zero!
# 如果断言失败，assert语句本身就会抛出AssertionError
# Traceback (most recent call last):
# ...
# AssertionError: n is zero!
# 
# 
# 程序中导出充斥这assert，和print()相比也好不到哪去，不过，启动Python解释器时可以用-O参数来关闭assert
# python -O err.py
# 注意：断言的开关‘-O’是英文大写字母O，不是数字0
# 关闭后，你可以把所有的assert语句当成pass来看



# logging
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
# 








