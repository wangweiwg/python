class Hello(object):
	def hello(self, name = 'world'):
		print('Hello, %s' %name)
# 当Python解释器载入hello模块时，就会依次执行改模块的所有语句,执行结果就是动态创建一个Hello的class对象，
# 测试如下：

# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型
# 就是class Hello。我们说class的定义是运动时动态创建的，而创建class的方法就是使用type()函数
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，
# 而无需通过class Hello(object)...的定义

def fn(self, name = 'world'):
	print('Hello，%s' %name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
# 要创建一个class对象，type()函数依次传入3个参数
# 1、class的名称
# 2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法
# 3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一
# 下class定义的语法，然后调用type()函数创建出class
# 正常情况下,我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身
# 支持运行期间动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用
# 编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常麻烦


# metaclass
# 除了使用type()动态创建类外，要控制类的创建行为，还可以使用metaclass
# metaclass，直译为元类，简单的解释就是：
# 当我们定义了类以后，就可以根据这个类创建出实例，所以，先定义类，然后创建实例
# 但是如果想创建出类？就必须根据metaclass创建出类，所以，先定义metaclass，然后创建类
# 连接起来就是：先定义metaclass，就可以创建类，最后创建实例
# 所以，metaclass允许创建类或者修改类，换句话说，可以把类看成是metaclass创建出来的实例
# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，不会碰到需要使用metaclass的情况，
# 所以，一下内容不懂也没关系，因为基本上用不到

# 先看个例子，这个metaclass可以给我自定义的MyList增加一个add方法
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass
# metaclass是类的模板，所以必须从type类型派生
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

# 有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass类定制类，传入关键字参数metaclass:
class MyList(list, metaclass = ListMetaclass):
	pass
# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过
# ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义
# __new__()方法接收到的参数依次是：
# 1、当前准备创建的类的对象
# 2、类的名字
# 3、类继承的父类集合
# 4、类的方法集合
# 测试一下MyList是否可以调用add()方法
L = MyList()
L.add(1)
print(L)
 


