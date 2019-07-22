# Python内建的filter()函数用于过滤序列
# 和map类似，filter也接收一个函数和一个序列。
# 不同的是，filter()把传入的函数依次作用于每一个元素，然后根据返回值是True还是False来决定保留还是丢弃该元素
# 例如：保留偶数
def is_even(n):
	return n % 2 == 0;
nums = list(filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9]));
print(nums);  # [2, 4, 6, 8]

# filter 返回的也是一个Iterator，也就是一个惰性序列