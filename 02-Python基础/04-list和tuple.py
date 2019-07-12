# list：列表
# list是Python内置的一种数据类型，list是一种有序的集合，可以随时添加和删除其中的元素
classmates = ['后裔', '典韦', '孙悟空', '黄忠'];

# 计算列表元素的个数
len(classmates);
# 可以使用索引访问列表中的元素
classmates[0];
# 如果要取最后一个元素可以使用-1
classmates[-1];
# 可以把元素插入到指定的位置
classmates.insert(1, '兰陵王');
# 要删除list末尾的元素，使用pop()方法, 返回的是删除的元素
classmates.pop();
# 要删除指定位置的元素，用pop(i)方法, 其中i是索引位置
classmates.pop(2);
# 要在list后面添加元素，用append()方法
classmates.append('要添加的元素');
# 要把某一个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[2] = '猪八戒';
# list里面的元素的数据类型也可以不用
# list里面的元素也可以是另一个list,可以是一个二维数组、三维数组、四维数组



# tuple
# 另一种有序的列表叫元组，tuple和list非常的相似，但是tuple一旦初始化就不能修改了，tuple没有append()、insert()
# 这样的方法，但是获取元素的方法和list是一样的，但是不能赋值成另外的元素
classmates2 = ('孙尚香', '虞姬', '伽罗');
# 只有一个元素的tuple时应该这么写, 加个逗号，否则会变为一个数字
classmates3 = (1, )
# tuple的元素不能变，实际上指的是元素的指向不能变，元素指向的list的内容是可以变的