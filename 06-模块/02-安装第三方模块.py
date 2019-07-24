# 在Python中，安装第三方模块，是通过包管理工具pip完成的
# 如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
# 如果是windows，参考安装Python一节的内容，确保安装时勾选了pip和
# Add python.exe to Path
# Mac或Linux上有可能并存Python 3.x和Python 2.x。因此对应的pip命令是pip3
# Python Imaging Library，这是Python下非常强大的处理图像的工具库。不过，PIL目前
# 只支持Python 2.7，并且有年头没有更新了。因此，基于PIL的Pillow项目开发非常活跃，
# 并且支持最新的Python 3。


# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，
# 必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，
# 安装Pillow的命令就是：
# pip install Pillow


# 安装常用模块
# 在使用Pyhton时，经常需要用到第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，
# Web框架Flask，科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容。

# 推荐使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了
# 许多非常有用的第三方库，安装上Anaconda，就相当于把数十个第三方模块自动安装好了。
# 可是从Anaconda官网下载GUI安装包，https://www.anaconda.com/distribution/
# 下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，并且Anaconda安装
# 的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录
# 安装好Anaconda后，重新打开命令行窗口，出入python，可以看到Anaconda的信息：
# 可以直接 import numpy 等已安装的第三方模块

# 模块搜索路径
# 当试图加载一个模块时，Python会在指定的路径下搜索对象的.py文件，如果找不到，就会报错
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存
# 放在sys模块的path变量中
# 如果要添加自己的搜索目录，有两种方法：
# 1、直接修改sys.path，添加要搜索的目录：
# import sys
# sys.path.append('/Users/***/my_py.scripts')
# 这种方法是在运行时修改，运行结束后失效
# 2、设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中，设置方式与设置Path
# 环境变量类似，注意只需要添加自己的搜索路径，Python自己本身的搜索路径不受影响。

