# -*- coding: utf-8 -*-
# dict
# dictionary, 在其他语言中也称map，使用键值存储，具有极快的查找速度
dict = {'name': 'wangwei', 'age': 57, 'gender': 'male'};
print(dict['name']);

# 如果key不存在，就会报错
# 可以通过in判断key是否存在
print('age' in dict);	# True
print('haha' in dict);	# False
# 还可以通过dict的get()方法，如果key不存在，可以返回None，或者自己指定的value
print(dict.get('name'));
print(dict.get('haha', -1));

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除，
# 并返回被删除的键对应的value
print(dict.pop('gender'));
print(dict);

# 注意：dict内部存放的顺序和key放入的顺序是没有关系的
# 和list比较，dict有以下几个特点：
# 1、查找和插入的速度极快，不会随着key的增加而变慢
# 2、需要占用大量的内存，内存浪费的多。
# 而list相反：
# 1、查找和插入的时间随着元素的增加而增加
# 2、占用空间小，浪费内存少。
# 综合来说，dict是用空间换取时间的一种方法。
# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，
# 需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，
# 那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。要保证hash的正确性，
# 作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。
# 而list是可变的，就不能作为key：


# set
# set和dict类似，也是一组key的集合，但不存储value，由于key不能重复，所以在set中没有重复的key
s = set([1, 2, 3]);
print(s);  # {1, 2, 3}
# 特点：
# 无序的
# 自动过滤重复的元素
# 通过add(key)方法可以添加元素到set中，可以重复添加，但是不会有效果
s.add(4);
print('添加之后是%s'%s);
# 通过remove(key)方法可以删除元素
s.remove(4);
print('删除之后是%s'%s);


# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集
# 并集等操作：
s1 = set([1, 2, 3]);
s2 = set([2, 3, 4]);
print('s1和s2的交集是：%s'%(s1 & s2));
print('s1和s2的并集是：%s'%(s1 | s2));

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，
# 同样不可以放入可变对象，因为无法判断两个对象是否相等，也就无法保证set内部不会有重复元素

# 再议不可变对象





