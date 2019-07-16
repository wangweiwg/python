# 切片
# 取一个list或tuple的部分元素是非常常见的操作：
L = ['1', '2', '3', '4', '5'];
print(L);
# 取前3个元素
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3，即索引0，1，2，正好是3个元素
L[0:3]; # [1, 2, 3]
# 如果第一个索引是0还可以省略
L[:3]; #[1, 2, 3]
# 也可以从索引1开始，取出2个元素出来：
L[1:3]; #[2, 3]
# 取倒数第一个元素
L[-1]; #[5]
# 同样支持倒数切片
L[-2:]; #[4, 5]
L[-2:-1]; #[4]

# 跳跃式切片，每两个取一个
L1 = list(range(100));
# 取前10个数，每两个取一次
L1[:10:2];
# 所有数，每5个取一次
L1[::5];

# tuple也是一种list，唯一区别是tuple不可变，因此，tuple也可以用切片操作，只是操作的结果仍是tuple
# 字符串也可以看成是一种list，每一个元素就是一个字符，因此，字符串也可以用切片操作，只是操作结果仍是字符串
'ABCDEFG'[:3]; #'ABC'
'ABCDEFG'[::2]; #'ACEG'


# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
	if len(s) == 0:
		return '';
	elif s[0] == ' ':
		return trim(s[1:]);
	elif s[-1] == ' ':
		return trim(s[:-1]);
	else:
		return s;
print('  hello World ');
print(trim('  hello World '));
print('  hello World ');
print('  hello World '.strip());

