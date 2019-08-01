# 读写文件是最常见的IO操作，Python内置了读写文件的函数，用法和C是兼容的
# 读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，现代操作系统不允许普通的程序直接操作磁盘，
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），然后，通过操作系统提供的接口从这个文件对象中读
# 取数据（读文件），或者把数据写入这个文件对象（写文件）。


# 读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标识符
f = open('./file.txt', mode='r', encoding='utf-8')
# 如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
# 如果打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
content = f.read()
# 最后一步是调用close()方法关闭文件，文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统
# 同一时间能打开的文件数量也是有限的：
f.close()
print(content)

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用，所以，为了保证无论是否出错都能正确地关闭
# 文件，我们可以使用 try ... finally 来实现
try:
	f1 = open('./file.txt', mode='r', encoding='utf-8')
	print(f1.read())
finally:
	if f1:
		f1.close()

# 但是每次都这么写实在是太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法
with open('./file.txt', mode='r', encoding='utf-8') as f2:
	print(f2.read())
# 这和前面的 try ... finally 是一样的，但是代码更加简洁，并且不必调用f.close()方法

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
# 每次最多读取size个字节的内容，另外，readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
# 因此，要根据需要决定怎么调用
# 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便：
print('1234567----')
f3 = open('./file.txt', mode='r', encoding='utf-8')
for line in f3.readlines():
	print(line.strip()) # 把末尾的'\n'删掉
f3.close()


# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节
# 流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲


# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等。用'rb'模式打开文件即可：
f4 = open('./git.png', mode='rb')
fPNG = f4.read()
print(fPNG)
f4.close()


# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件:
f5 = open('./gbk.txt', 'r', encoding='gbk')
f5Content = f5.read()
print(f5Content)
f5.close()
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
open('./file.txt', mode='r', encoding='gbk', errors='ignore')


# 写文件
# 写文件和读文件是一样的，唯一的区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本或写二进制文件：
f6 = open('./write.txt', 'w', encoding='utf-8')
f6.write('写进去了吗？')
f6.close()
# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据
# 写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部
# 写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
with open('./write.txt', 'w', encoding='utf-8') as f7:
	f7.write('使用with as就不用自己调用close函数了')

# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成制定个的编码
# 细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
f8 = open('./write.txt', 'a', encoding='utf-8')
f8.write('\n新加的')
f8.close()



