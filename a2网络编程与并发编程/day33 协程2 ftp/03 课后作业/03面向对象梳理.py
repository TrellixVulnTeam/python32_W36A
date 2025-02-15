三、面向对象
1 封装
	00 类的概念
		(1)类的定义
		(2)类的实例化
		(3)类的基本结构
		(4)类的命名
			推荐大驼峰命名法 MyCar
		
	01 对象的操作
		# 封装:
			# 1.私有 : 在类内可以互相访问,在类外不能访问
			# 2.公有 : 在类内或者类外都可以访问

		# 类中成员:
			# 1.成员属性
			# 2.成员方法
			
		# 绑定方法:
			# 1.绑定到对象 : 当对象去调用类中成员方法时,系统会默认把该对象当成参数传递给该方法 self
			# 2.绑定到类   : 当对象或者类去调用类中成员方法时,系统会默认把该类当成参数传递给该方法  @classmethod  cls

		# 使用方式:
			# 对象.成员属性
			# 对象.成员方法
			
		__dict__ 获取类对象的内部成员
		print(obj.__dict__)
		print(MyCar.__dict__)
		
		对象动态添加公有成员属性
		对象动态添加公有成员方法	
	
	02 类的操作
		# 对比 对象和类之间的不同
		# 1.类中的无参方法默认只能类来调用,对象无法调取
		# 2.对象可以调用类中的成员,反过来,类不能调用对象中的成员
		# 3.每创建一个对象都会在内存中占用一份空间,对象之间是彼此独立的;
		类和对象是两个独立的内存空间
		
		类动态添加公有成员属性
		类动态添加公有成员方法
		
	03 私有成员和成员删除
		使用类中的公有方法,间接访问私有成员
		
		# 1.对象可以访问类中的公有成员,但是无权修改或者删除该类中的成员
		# 2.对象在访问成员时,优先访问该对象自己的成员,如果没有再访问类的,类如果也没有直接报错;
			类和对象是两个独立的内存空间
			
		# 注意: 对象无法调无参方法!! 
		# 返回来,类可以调用对象的绑定方法么? 可以!!  #把对象当做实参传递即可

2 继承
	01 单继承
		# 一个类除了自身所拥有的属性方法之外,还获取了另外一个类的成员属性和方法 是一种继承关系
		# 被继承的类叫做父类(基类,超类),继承的类叫做子类(衍生类)
		# 在python中所有类都继承object这个父类
		# 继承: (1) 单继承  (2) 多继承
		
		子类可以调用父类的公有成员
		子类不能调用父类的私有成员
		子类可以重写父类的同名公有方法
	
	02 多继承
		class Daughter(Father,Mother):
			pass
			
		# (1)super本身是一个类 super()是一个对象 用于调用父类的绑定方法
		# (2)super() 只应用在绑定方法中,默认自动传递self对象 (前提:super所在作用域存在self)
		# (3)super用途: 解决复杂的多继承调用顺序	
	
	03 菱形继承
		# mro: 方法解析顺序 (c3算法计算的)
		# 语法: 类.mro() => 列表
		# m :method
		# r :resolution 
		# o :order
		# super 会自动根据mro列表返回出来的顺序关系,依次调用 
		# super作用:专门用于解决复杂的多继承调用顺序关系;依照mro返回的列表顺序,依次调用;
		# super调用的顺序:会按照c3算法的广度优先原则进行调用
		# super传参:会默认在调用方法时,传递该对象参数;
		# super()是一个对象  谁调传谁(传对象)  这里是Children类的对象obj调，就把obj当参数传递
		
		issubclass与isinstance
		issubclass 判断类的子父关系(应用在类与类之间)
		只要在一条继承链上(后代)满足关系即可
		如果元组当中有一个父类满足,即返回真

		isinstance 判断对象的类型  (应用在类与对象之间)
		只要在一条继承链上（后代）满足关系即可
		如果元组当中有一个类满足,即返回真	
	
	04 构造方法
			# 触发时机：实例化对象,初始化的时候触发
			# 功能：为对象添加成员（属性或方法）
			# 参数：参数不固定,至少一个self参数
			# 返回值：无	

3 多态
	01 多态
		多态: 不同的子类对象调用相同的父类方法,得到不同的执行结果
			继承 重写父类的方法
		调用方:不同的子类对象.
		方法:相同的父类方法
		返回:不同的结果 	
	
	02 单态
		单态模式 : 同一个类,无论实例化多少次,都有且只有一个对象

		每创建一个对象,就会在内存中多占用一份空间
		为了节省空间,提升执行效率,使用单态模式
		应用场景:只是单纯调用类中的成员,而不会额外为当前对象添加成员（只读不写）;
		
		class Singleton():
			__obj = None
			def __new__(cls):
				if cls.__obj is None:
					cls.__obj = object.__new__(cls)
				return cls.__obj	
	
	03 __new__
		  触发时机：实例化类生成对象的时候触发(触发时机在__init__之前)
		  功能：控制对象的创建过程
		  参数:至少一个cls接受当前的类,其他根据情况决定
		  返回值：通常返回对象或None
		  
		  001 __new__ 触发时机要快于 __init__
				__new__  创建对象
				__init__ 初始化对象
		  002 __new__的参数要和__init__参数一一对应
		  003 如果__new__ 没有返回对象或者返回的是其他类的对象,不会调用构造方法.
		      只有在返回自己本类对象的时候,才会调用构造方法.
		  
		  基本使用
		  class MyClass1():
			def __new__(cls):
				# print(cls)	
				
				# 1.返回本类对象
				# """类.成员方法(类)"""
				# return object.__new__(cls)
				
				# 2.返回其他类的对象
				# return obj2
				
				# 3.不返回对象,None
				return None		
			
			obj = MyClass1()
	
	04 __del__
		# 触发时机:当对象被内存回收的时候自动触发
		  # [1.页面执行完毕回收所有变量 
		   # 2.所有对象被del的时候（指的单个对象的引用次数为0）]
		# 功能：对象使用完毕后资源回收
		# 参数：一个self接受对象
		# 返回值：无	
	
	05 __str__
		# 触发时机: 使用print(对象)或者str(对象)的时候触发
		# 功能:     查看对象
		# 参数:     一个self接受当前对象
		# 返回值:   必须返回字符串类型
		
	06 __repr__
		# 触发时机: 使用repr(对象)的时候触发
		# 功能:     查看对象,与魔术方法__str__相似
		# 参数:     一个self接受当前对象
		# 返回值:   必须返回字符串类型

4 魔术方法 异常
	01 __call__
		# 触发时机：把对象当作函数调用的时候自动触发  obj() 对象加小括号
		# 功能: 模拟函数化操作
		# 参数: 参数不固定,至少一个self参数
		# 返回值: 看需求
		
		(1) 基本语法
			class MyClass():
				def __call__(self):
					print("__call__魔术方法被触发 ... ")

			obj = MyClass()
			obj()
			
		(2) 利用__call__魔术方法做统一调用
			把成员方法放在__call__中统一调用
		
		(3) 模拟整型强转操作
	
	02 __bool__
			# 触发时机：使用bool(对象)的时候自动触发
			# 功能：强转对象  (把obj对象转换成bool)
			# 参数：一个self接受当前对象
			# 返回值：必须是布尔类型
			# 类似的还有如下等等(了解):
				# __complex__(self)      被complex强转对象时调用
				# __int__(self)          被int强转对象时调用
				# __float__(self)        被float强转对象时调用
				
			class MyClass():
				def __bool__(self):
					return True
			obj = MyClass()
			print(bool(obj))
			
	03 __add__
		#__add__ 魔术方法  (与之相关的__radd__ 反向加法)
			# 触发时机：使用对象进行运算相加的时候自动触发
			# 功能：对象运算
			# 参数：二个对象参数
			# 返回值：运算后的值
		# 类似的还有如下等等(了解):
			# __sub__(self, other)           定义减法的行为：-
			# __mul__(self, other)           定义乘法的行为：
			# __truediv__(self, other)       定义真除法的行为：/
			
	04 __len__
		# 触发时机：使用len(对象)的时候自动触发 
		# 功能：用于检测对象中或者类中某个内容的个数
		# 参数：一个self接受当前对象
		# 返回值：必须返回整型			
	
	05 魔术属性
		001 __dict__
			获取对象或类的内部成员结构
			dic = Sasuke.__dict__
			dic = obj.__dict__
			
		002 __doc__  
			获取对象或类的内部文档
			print(Sasuke.__doc__)
			print(obj.__doc__)
			
		003 __name__  
			获取类名函数名,返回str
			
		004 __class__ 
			获取当前对象所属的类
			print(obj.__class__)
			
		005 __bases__ 
			获取一个类直接继承的所有父类,返回元组
			print(Sasuke.__bases__)
				
	06 异常
		001 常见异常
			# IndexError                索引超出序列的范围
			# KeyError                  字典中查找一个不存在的关键字
			# NameError                 尝试访问一个不存在的变量
			# IndentationError          缩进错误
			# AttributeError            尝试访问未知的对象属性
			# StopIteration             迭代器没有更多的值
			# AssertionError			 断言语句（assert）失败
			
		002 异常处理的语法
			a
			# try .. except ..  来抑制错误
			# 把有可能报错的代码放到try这个代码块当中,
			# 如果有报错,直接执行except这个代码块
			# 如果没有报错,不执行except这个代码块

			# 在异常处理当中,所有的异常错误类都继承  
			# BaseException   Exception 普通异常的父类(了解)
			
			b
			# 处理生成器的异常报错
			try:
				pass				
				# 给StopIteration这个类创建出来的对象起一个别名叫e
				# 当你打印对象时,会触发内部__str__方法,通过一系列的调用,返回出最后的返回值
			except StopIteration as e:
				# 可以获取返回值
				print(e)
				
			# 1 .try .. except .. else ..
			# 当try这个代码块当中没有报错的时候,执行else这个分支
			# 如果try代码块有报错,就不执行else这个分支
			
			# 2.try .. finally ... 无论代码是否报错,都必须要执行的代码写在finally这个代码块当中
			# 场景:应用在异常环境下,保存数据或者关闭数据库等操作,
			# 必须要在数据库程序崩溃之前执行的代码写在finally代码块中;
			
			3.try .. except .. else .. finally .. 
			
			c 主动抛异常
			# BaseException  所有异常类的父类
			# Exception      普通异常类的父类
			# raise + 异常错误类 / 异常错误类对象

			# (1) raise 基本语法
			# raise KeyError
			# raise KeyError()
			
			# (2) 自定义异常错误类
			   必须继承异常类的父类 BaseException
			   例子:模拟解释器报错			

5 装饰器
	01 装饰器
		装饰器 : 在不改变原有代码的前提下,为原函数扩展新功能
		@符号 装饰器的标识符 :
		# (1) 自动把下面修饰的原函数当成参数传递给装饰器
		# (2) 把返回的新函数去替换原函数
		
		(1) 装饰器的原型
		(2) @符号的使用
		(3) 装饰器的嵌套
		(4) 带有参数的装饰器
			原函数和新函数的参数和返回值要保持一一对应
		(5) 带有参数返回值的装饰器
		(6) 使用类装饰器
		(7) 带有参数的函数装饰器
		(8) 带有参数的类装饰器
		
		分类:
		1 函数装饰器
			1 无参数
			2 有参数
		2 类装饰器
			1 无参数
			2 有参数
			
		写法:
		# 01 定义装饰器函数
		def kuozhan(_func):
			def newfunc(who,where,eat):  #新函数3个形参 和原函数参数一致
				print("前 ... 文质彬彬")
				_func(who,where,eat)  #原函数3个实参
				print("后 ... 大发")
			return newfunc

		# 02 给原函数加装饰器
		@kuozhan
		# func = kuozhan(func)  #把原函数当成参数传递给装饰器函数
		# func = newfunc        #把返回的新函数去替换原函数  定义装饰器
		# func() = newfunc()    #调用装饰器

		# 03 定义原函数
		def func(who,where,eat):  #原函数3个形参
			print("{who}在{where}吃{eat}".format(who=who,where=where,eat=eat)  )

		# 04 调用加了装饰器的原函数	
		func("假率先","浴缸","榴莲") # <=> newfunc()
		
		步骤:
		01 定义装饰器函数
		02 给原函数加装饰器  @
		03 定义原函数
		04 调用加了装饰器的原函数

	02 类中的方法
			# (1)普通无参方法
			# (2)绑定方法: (1)绑定到对象 (2)绑定到类
			# (3)静态方法:无论是对象还是类调用静态方法,都不会默认传递任何参数
			
			# 绑定到类方法调用
			无论对象还是类都可以调用,默认传递的是类

6 反射
	01 属性
		# 可以把方法变成属性 : 可以动态的控制属性的获取,设置,删除相关操作
		# @property  获取属性
		# @方法名.setter  设置属性
		# @方法名.deleter 删除属性
		
		# 方法一  是同一个方法名 不同的装饰器
		# 方法二   不同的方法名  不用装饰器
			# 参数的顺序: 获取 , 设置  , 删除
			username = property(get_username , set_username  , del_username )
			
	02 反射
		通过字符串操作类 对象 或者 模块中的相关成员的操作
		# hasattr() 检测对象/类是否有指定的成员
		# getattr() 获取对象/类成员的值(内存地址)
			# 如果获取的值不存在,可以设置第三个参数,防止报错
			# 通过类进行反射 (反射出来的是普通方法-非绑定方法)
			# 通过对象进行反射 (反射出来的是绑定方法)
		# setattr() 设置对象/类成员的值
		# delattr() 删除对象/类成员的值 
		
		part1 通过字符串反射类对象中的成员
		part2 通过字符串反射模块中的成员















