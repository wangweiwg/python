# 我们前面编写的所有Python程序，都是执行单任务的进程，也就是只有一个线程。如果我们要同时执行多个任务怎么办？
# 解决方案有两个：
# 1、一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务
# 2、另外一种是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务
# 总结一下就是，多任务的实现有3种方式：
# 多进程模式；
# 多线程模式；
# 多进程+多线程模式。
# 同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，有时，任务1必须暂停等待任务2完成后才
# 能继续执行，有时，任务3和任务4又不能同时执行，所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单
# 线程的程序。
# 因为复杂度高，调试困难，所以，不是迫不得已，我们也不想编写多任务。但是，有很多时候，没有多任务还真不行。想想在
# 电脑上看电影，就必须由一个线程播放视频，另一个线程播放音频，否则，单线程实现的话就只能先把视频播放完再播放音频，
# 或者先把音频播放完再播放视频，这显然是不行的。
# Python既支持多进程，又支持多线程，我们会讨论如何编写这两种多任务程序。




# 多进程
# 要让Python程序实现多进程(multiprocessing)，我们先了解操作系统的相关知识
# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊，普通的函数调用，调用一次，返回一次，但是fork()调用
# 一次，返回两次，因为操作系统自动把当前进程(称为父进程)复制了一份（称为子进程），然后，分别在父进程和子进程
# 内返回
# 子进程永远返回0，而父进程返回子进程的ID，这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记
# 下每个子进程的ID，而子进程只需调用getppid()就可以拿到父进程的ID
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程
import os
print('Process (%s) start...' % os.getppid())
# Only fork on Unix/Linux/Mac
# pid = os.fork()
# if pid == 0:
# 	print('I am child process (%s) and my parent is %s' %(os.getpid(), os.getppid()))
# else:
# 	print('I (%s) just created a child pricess (%s)' %(os.getpid(), pid))


# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，
# 所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
# 
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由
# 父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。


# multiprocessing
# 如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows
# 上无法用Python编写多进程的程序？
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process
import os
# 子进程要执行的代码
def run_proc(name):
	print('Run child prcess %s (%s) ...' %(name, os.getpid()))

if __name__ == '__main__':
	print('Parent process %s.' % os.getpid())
	p = Process(target = run_proc, args = ('test', ))
	print('Child process will start')
	p.start()
	p.join()
	print('Child process end')

# 创建子进程时，只需要传入一个执行函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还简单
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步


# Poll
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from mulitiprocessing import Poll
import os, time, random
 




