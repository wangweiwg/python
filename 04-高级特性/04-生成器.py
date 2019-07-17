# 生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个
# 包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那么后面绝大多数
# 元素占用的空间都白白浪费了。
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不
# 必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# 创建一个generator，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)];
print(L);

g = (x * x for x in range(10));
print(g);
# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator
# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值:
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));
print(next(g));

# 前边说过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后
# 一个元素，没有更多的元素时，抛出StopIteration的错误。
# 这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
g1 = (x for x in range(10));
for n in g1:
	print(n);
# 因此，基本不会使用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
# 如果推算的算法比较复杂，用类似类表生成式的for循环无法实现的时候，还可以用函数来实现。
# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
	n, a, b = 0, 0, 1;
	while n < max:
		print(b);
		a, b = b, a + b;
		n = n + 1;
	return 'done';
fib(6);

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续
# 任意的元素，这种逻辑其实非常类似generator
# 要把上面的fib函数变成generator，只需要把print(b); 改为 yield b 就可以了:
def fib1(max):
	n, a, b = 0, 0, 1;
	while n < max:
		yield b;
		a, b = b, a + b;
		n = n + 1;
	return 'done';
# 这就是定义generator的另一种方法，如果一个函数定义中包含yield关键字，那么这个函数就不再是一个
# 普通函数，而是一个generator：
f1 = fib1(6);
print(f1);

# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或最后一行函数语句
# 就返回。而变成generator的函数在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回
# 的yield语句处继续执行。
# 定义一个generator，依次返回数字1, 3, 5
def getNum():
	print('step 1');
	yield 1;
	print('step 2');
	yield 3;
	print('step 3');
	yield 5;
# 首先生成一个generator对象，然后用next()函数不断获得下一个返回值：
o = getNum();
print(next(o));
print(next(o));
print(next(o));





