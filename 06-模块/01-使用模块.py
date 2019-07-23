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
	test();