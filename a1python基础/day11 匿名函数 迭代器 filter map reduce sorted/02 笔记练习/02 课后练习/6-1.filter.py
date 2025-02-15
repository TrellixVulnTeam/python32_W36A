# ### filter
# filter(func,iterable)
# 功能:
# 	过滤数据
# 	在自定义的函数中
# 		如果返回True,该数据保留
# 		如果返回False,该数据舍弃
#
# 参数:
# 	func:自定义函数
# 	iterable:可迭代对象(容器类型数据 range对象  迭代器)
#
# 返回值:
# 	迭代器

# 1.只要列表中所有的偶数
lst = [1,2,34,5,65,6,56,7,56,756,7567,11]

#方法1  普通方法
lst = [1,2,34,5,65,6,56,7,56,756,7567,11]
lst_new = []
for i in lst:
	if i % 2 == 0:
		lst_new.append(i)
print(lst_new)  #[2, 34, 6, 56, 56, 756]
print('------------------------1')

#方法2 filter改写
lst = [1,2,34,5,65,6,56,7,56,756,7567,11]
def func(n):
	if n % 2 == 0:
		return True
	else:
		return False

it = filter(func,lst)
print(list(it))
#[2, 34, 6, 56, 56, 756]
print('------------------------2')

#方法3 filter lambda
lst = [1,2,34,5,65,6,56,7,56,756,7567,11]
it = filter(lambda n:True if n%2 ==0 else False,lst)
print(list(it))  #[2, 34, 6, 56, 56, 756]
print('------------------------3')
































