# 使用模块
# Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用


# 可以让文件直接运行在Unix/Linux/Mac上运行，
#!/usr/bin/env python3
# 表示文件本身使用标准UTF-8编码
# -*- coding: utf-8 -*-

# 字符串表示模块的文档注释，任何模块代码的第一个字符串都视为模块的文档注释
'a test module'

# 使用__author__变量把作者写进去，这样公开源码后别人可以瞻仰你的大名，哈哈哈~~~
__author__ = 'wang wei'

# 使用sys模块的第一步就是导入该模块
import sys;
# 导入模块后，我们就有了变量sys指向该模块，利用sys这个变量，就可以访问sys模块的所有功能
# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远当前文件的名称，


def test():
	args = sys.argv;
	print(sys);
	if len(args) == 1:
		print('有一个参数，args[0] = %s' %args[0]);
	elif len(args) == 2:
		print('有两个参数，args[0] = %s args[1] = %s' %(args[0], args[1]));
	else:
		print('args的参数有%s个' %len(args));

if __name__ == '__main__':
	# test();
# 当我们在命令行运行Python文件时，Python解释器把一个特殊变量__name__置为__main__，而如果在其它地方
# 导入该文件模块时，if判断将失败，因此，这种if测试可以让一个模块通过命令运行时执行一些额外的代码，最
# 常见的就是运行测试


# 作用域
# 在一个模块中我们可能定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望
# 仅仅在模块内部使用，在Python中，是通过_前缀来实现的。
# 正常的函数和变量名是公开的(public)，可以被直接引用，比如abc，x123，PI等
# 类似__xxx__这样的变量是特殊变量，可以直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，
# 模块中定义的文档注释也可以用特殊变量__doc__访问，自己定义的变量一般不要用这种变量名
# 类似_xxx和__xxx这样的函数或变量就是非公开的(private)，不应该被直接引用，比如_abc，__abc等
# 之所以说，privata函数和变量不应该被直接引用，而不是不能被直接引用，是因为Python并没有一种方法可以完全限制
# 访问函数或变量，但是，从编程习惯上不应该引用private函数或变量。


# private函数或变量不应该被别人引用，那有什么用呢？
# 例如：
def _private1(name):
	return 'Hello，%s' % name

def _private2(name):
	return 'Hi，%s' % name

def greeting(name):
	if len(name) > 3:
		return _private1(name)
	else:
		return _private2(name)
# 在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用gretting()函数
# 不用关心内部的private函数细节，这也是一种非常有用的代码封装和抽象的方法，即：
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public