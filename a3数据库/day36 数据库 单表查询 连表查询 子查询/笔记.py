# ### part 单表查询
# """ select ... from ... where ... group by ... having ... order by ... limit ...  """

# 一.where 条件的使用
	# """
		# 功能: 对表中的数据进行筛选和过滤
		# 语法:
			# 1.判断的符号
			# = (!= <>不等于) > >= < <=
			# 2.拼接不同的条件的关键字
			# and or not 
			# 3.查询对应的区间值
			# between 小值 and 大值 [小值,大值]   查询两者之间的范围值
			# 4.查询具体在哪个范围中
			# in(1,21,333,444) 指定范围
			# 5.模糊查询 like 
			    # % 通配符  匹配0个或者多个字符
				# _ 通配符  匹配一个字符
				# like "%b"  匹配以b结尾的任意长度的字符串
				# like "b%"  匹配以b开头的任意长度的字符串
				# like "%b%" 匹配字符串中含有b的任意长度的内容
				# like "__b" 匹配总长度为3个字符,任意内容的字符串,并且以b结尾
				# like "b_"  匹配总长度为2个字符,任意内容的字符串,并且以b开头
				
		# 注意点:
			# where 后面不能写max(name),不能有(),写别名max_name
	# """
	
	# 1. 查询部门是sale的所有员工姓名:
	select emp_name from employee where post="sale";

	# 2. 部门是teacher , 收入大于10000的所有数据
	select * from employee where post = "teacher" and salary > 10000;
	
	# 3. 收入在1万到2万之间的所有员工姓名和收入
	select emp_name,salary from employee where salary between 10000 and 20000;
	
	# 4. 收入不在1万到2万之间的所有员工姓名和收入
	select emp_name,salary from employee where salary not between 10000 and 20000;
	
	# 5. 查看岗位描述为NULL的员工信息
	select emp_name from employee where post_comment = null;
	select emp_name from employee where post_comment = '';
	select emp_name from employee where post_comment is null;  #正确 null是关键字，不能用= 要用is
	
	# 6. 查看岗位描述不为NULL的员工信息
	select emp_name from employee where post_comment is not null;
	
	# 7. 查询收入是3000 ,4000 ,5000,8300 所有员工的姓名和收入
	select emp_name,salary from employee where salary in(3000,4000,5000,8300);
	select emp_name,salary from employee where salary = 3000 or salary=4000 or salary=5000 or salary=8300;
	
	# 8. 查询收入不是3000 ,4000 ,5000,8300 所有员工的姓名和收入
	select emp_name,salary from employee where salary not in(3000,4000,5000,8300);

	# 9. 以on结尾的员工名搜一下
	select emp_name from employee where emp_name like "%on";
	select emp_name from employee where emp_name like "ji%";
	select emp_name from employee where emp_name like "_le_";
	
	# 10. 统计员工一年的年薪
	select concat(" 姓名: ",emp_name,"  收入:  ",salary) from employee;
	
	# 计算年薪,可以在mysql中使用四则运算符 + - * / 
	select concat(" 姓名: ",emp_name,"  收入:  ",salary * 12) from employee;
	select concat_ws("  :  ",emp_name,salary*12 ) from employee;
	
	# 11. 查询部门的种类
	# distinct  返回唯一不同的值
	select distinct(post)  from employee;
	
	
# 二.group by 子句 分组分类
	# """group by 字段,对数据进行分类, by后面接什么字段,select后面就搜什么字段"""
	#group by后面的字段.select后面必须有(如果有聚合函数的话,select后面可以只接聚合函数).    #注意点
	#select后面有的,group by后面可以没有,也可以有,需要看情况
	# 
	select sex from  employee group by sex;
	
	#group by的规律
	select sex,count(*),id from  employee group by sex;  #会报错
	# this is incompatible with sql_mode=only_full_group_by
	# 原因:sex和id是一对多,如果是一对一是不报错的
	
	# 如果sex和id是一对多,用group_concat(id)即可
	mysql> select sex,count(*),group_concat(id) from  employee group by sex;
	# +--------+----------+------------------------+
	# | sex    | count(*) | group_concat(id)       |
	# +--------+----------+------------------------+
	# | male   |       10 | 2,3,4,5,1,7,8,17,15,14 |
	# | female |        8 | 18,16,13,12,11,10,9,6 
	
	select emp_name,count(*),id from  employee group by id;
	select * from  employee group by id;   
	# 这里不报错的原因:id这个字段是unique或者主键
	# +--------------+----------+----+
	# | emp_name     | count(*) | id |
	# +--------------+----------+----+
	# | egon         |        1 |  1 |
	# | alex         |        1 |  2 |
	# | wupeiqi      |        1 |  3 |
	# | yuanhao      |        1 |  4 |
	
	# 结论:
	# 1 group by 后面的id如果是unique或者主键,select可以是*或者任意字段
		# select后面有的,group by后面可以没有
	# 2 group by 后面的sex如果不是unique或者主键
		# group by后面是sex,select后面只能是sex或者聚合函数,如果select后面写了id等其他字段
		# 直接写,会报错  this is incompatible with sql_mode=only_full_group_by
		# 此时用group_concat(id)就不会报错,可以解决一对多
		
		
	
	# group_concat 按照分组把对应字段拼在一起(适用于一对多);
	select group_concat(emp_name),post from  employee group by post;
	# 查询每个部门的员工姓名   (一个部门有多个员工)
	# | post                                    | group_concat(emp_name)                                  |
	# +-----------------------------------------+---------------------------------------------------------+
	# | operation                               | 程咬铁,程咬铜,程咬银,程咬金,张野                        |
	# | sale                                    | 丫丫,格格,星星,丁丁,歪歪                                |
	# | teacher                                 | 成龙,jinxin,jingliyang,liwenzhou,yuanhao,wupeiqi,alex   |
	# | 老男孩驻沙河办事处外交大使              | egon     

	select post,emp_name from employee group by post,emp_name;  #分组2次
	# | post                                    | emp_name   |
	# +-----------------------------------------+------------+
	# | operation                               | 张野       |
	# | operation                               | 程咬金     |
	# | operation                               | 程咬铁     |
	# | operation                               | 程咬铜     |
	# | operation                               | 程咬银     |
	# | sale                                    | 丁丁       |
	# | sale                                    | 丫丫       |
	# | sale                                    | 星星       |
	# | sale                                    | 格格       |
	# | sale                                    | 歪歪       |
	# | teacher                                 | alex       |
	# | teacher                                 | jingliyang |
	# | teacher                                 | jinxin     |
	# | teacher                                 | liwenzhou  |
	# | teacher                                 | wupeiqi    |
	# | teacher                                 | yuanhao    |
	# | teacher                                 | 成龙       |
	# | 老男孩驻沙河办事处外交大使              | egon   

	
	# 聚合函数
		# count 统计总数 *所有
		select count(*) from employee;
		# max  统计最大值
		select max(salary) from employee;
		# min  统计最小值
		select min(salary) from employee;
		# avg  统计平均值
		select avg(salary) from employee;
		# sum  统计总和
		select sum(salary) from employee;
		
	# 1. 查询部门名以及各部门的平均薪资
	select avg(salary),post from employee group by post;  #各部门- group by
	
	# 2. 查询部门名以及各部门的最高薪资
	select max(salary),post from employee group by post;
	
	# 3. 查询部门名以及各部门的最低薪资
	select min(salary),post from employee group by post;
	
	# 4. 查询公司内男员工和女员工的个数
	select count(*),sex from employee group by sex;  #个数 count(*)  +group by
	
	# 5. 查询部门名以及部门包含的所有员工名字  (一个部门有多个员工)
	select group_concat(emp_name),post from employee group by post;
	
	# 6 可以group by 两个字段,就可以同时搜索两个字段
	select emp_name,post from employee group by post ,emp_name;
	
	# group by经常和聚合函数搭配使用
	

# 三.having 在数据分类分组之后,对数据进行二次过滤,一般配合group by来使用的;
	# 找出各部门平均薪资,并且大于10000
	select post , avg(salary) from  employee group by post having avg(salary) > 10000  #各部门-group by  大于-having

	# 1.查询各岗位(部门)内包含的员工个数小于2的岗位名、岗位内包含员工名字、个数     #各部门-group by  小于-having
	select post , group_concat(emp_name), count(*) from employee group by post having count(*) < 2;
	# 一个部分含有多个员工，用group_concat
	
	# 2.查询各岗位(部门)平均薪资小于10000的岗位名、平均工资
	select post , avg(salary) from employee group by post having avg(salary) < 10000
	
	# 3.查询各岗位(部门)平均薪资大于10000且小于20000的岗位名、平均工资
	select post, avg(salary) from employee group by post having avg(salary) between 10000 and 20000  #左闭右闭
	select post, avg(salary) from employee group by post having avg(salary) > 10000 and  avg(salary) < 20000;
	
	
# 四.order by 排序 , 按照某字段排序
	order by age asc (升序) (不写默认升序) order by age desc (降序)
	# 按照年龄从小到大排序
	select * from employee order by age;
	
	# 按照年龄从大到小排序
	select * from employee order by age desc;
	
	# 1. 查询所有员工信息，先按照age升序排序，如果age相同则按照hire_date降序排序
	select * from employee order by age asc ,  hire_date desc;
	
	# 2. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资升序排列
	select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) asc
	
	# 3. 查询各岗位平均薪资大于10000的岗位名、平均工资,结果按平均薪资降序排列
	select post,avg(salary) from employee group by post having avg(salary) > 10000 order by avg(salary) desc
	
# 五.limit 限制查询条数 (应用在分页)
	# """ limit m,n m代表从第几条数据开始查, n 代表查几条  m=0 代表的是第一条数据"""
	select * from employee limit 0,10   # 0代表的是第一条数据
	select * from employee limit 10,10  # 10代表的是第十一条数据
	select * from employee limit 20,10  # 20代表的是第二十一条数据
	
	# limit + num  num => 搜索多少条数据
	select * from employee limit 1
	
	# 搜索这个表里面最后一条数据
	select * from employee order by id desc limit 1
	
	# 搜索这个表里面最后五条数据
	select * from employee order by id desc limit 5
	
	
# 六.mysql 当中可以使用正则表达式 (不推荐,效率低)
	select * from employee where  emp_name regexp ".*on$"; # mysql中无法识别?
	select * from employee where  emp_name regexp "^程.*";
	select * from employee where  emp_name regexp "^程.*金";
	
# `### part2  多表查询
	# 1.内联接 :  inner join  :  两表或者多表之间,把满足条件的所有数据查询出来 (多表之间共同拥有的数据会被查询出来)
	#   把两个表的字段合在一起  比如：表a有5个字段，表b有2个字段，合在一起就是7个字段。
		# 两表联查
		select 字段 from 表1 inner join 表2 on 必要的关联条件   #on后面只写必要的关联条件,其他条件写在where后
		# 多表联查
		select 字段 from 表1 inner join 表2 on 必要的关联条件1 inner join 表3 on 必要的关联条件2 
		
	select * from employee inner join department on employee.dep_id = department.id;
	
	# as 起别名
	select * from employee as e inner join department as d on e.dep_id = d.id;
	
	# 也可以省略as (不推荐,容易看不清)	
	select * from employee e inner join department d on e.dep_id = d.id;
	
	# where 写法默写是内联接( 等同于inner join )
	select * from employee,department where employee.dep_id = department.id;  #内连接1
	select * from employee as e ,department as d where e.dep_id = d.id;  #内连接2
	# | id | name      | sex    | age  | dep_id | id   | name         |
	# +----+-----------+--------+------+--------+------+--------------+
	# |  1 | egon      | male   |   18 |    200 |  200 | 技术         |
	# |  2 | alex      | female |   48 |    201 |  201 | 人力资源     |
	# |  3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源     |
	# |  4 | yuanhao   | female |   28 |    202 |  202 | 销售         |
	# |  5 | liwenzhou | male   |   18 |    200 |  200 | 技术 
		
	# 2.外联接 :  left join左联接  / right join 右联接
	# (1)left  join左联接 : 以左表为主,右表为辅,完整查询左表所有数据,右表没有的数据补null
	select * from employee left join department on employee.dep_id = department.id;	
	# | id | name       | sex    | age  | dep_id | id   | name         |
	# +----+------------+--------+------+--------+------+--------------+
	# |  1 | egon       | male   |   18 |    200 |  200 | 技术         |
	# |  5 | liwenzhou  | male   |   18 |    200 |  200 | 技术         |
	# |  2 | alex       | female |   48 |    201 |  201 | 人力资源     |
	# |  3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源     |
	# |  4 | yuanhao    | female |   28 |    202 |  202 | 销售         |
	# |  6 | jingliyang | female |   18 |    204 | NULL | NULL   
	
	# (2)right join右联接 : 以右表为主,左表为辅,完整查询右表所有数据,左表没有的数据补null
	select * from employee right join department on employee.dep_id = department.id;
	# | id   | name      | sex    | age  | dep_id | id   | name         |
	# +------+-----------+--------+------+--------+------+--------------+
	# |    1 | egon      | male   |   18 |    200 |  200 | 技术         |
	# |    2 | alex      | female |   48 |    201 |  201 | 人力资源     |
	# |    3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源     |
	# |    4 | yuanhao   | female |   28 |    202 |  202 | 销售         |
	# |    5 | liwenzhou | male   |   18 |    200 |  200 | 技术         |
	# | NULL | NULL      | NULL   | NULL |   NULL |  203 | 运营  
	
	# 3.全联接 :  union #合并  #结果是全连接 = 左连接+右连接
	select * from employee left join department on employee.dep_id = department.id
	union
	select * from employee right join department on employee.dep_id = department.id;
	# | id   | name       | sex    | age  | dep_id | id   | name         |
	# +------+------------+--------+------+--------+------+--------------+
	# |    1 | egon       | male   |   18 |    200 |  200 | 技术         |
	# |    5 | liwenzhou  | male   |   18 |    200 |  200 | 技术         |
	# |    2 | alex       | female |   48 |    201 |  201 | 人力资源     |
	# |    3 | wupeiqi    | male   |   38 |    201 |  201 | 人力资源     |
	# |    4 | yuanhao    | female |   28 |    202 |  202 | 销售         |
	# |    6 | jingliyang | female |   18 |    204 | NULL | NULL         |
	# | NULL | NULL       | NULL   | NULL |   NULL |  203 | 运营    
		
# ### part3 子查询 
	# """
	# 子查询: 嵌套查询
		# (1) sql语句当中又嵌套了另外一条sql,用括号()进行包裹,表达一个整体
		# (2) 一般用在from子句,where子句... 身后,表达一个条件或者一个表
		# (3) 速度快慢: 单表查询 > 联表查询 > 子查询;
		# 注意点:  子查询语句写在from后,必须要给子查询语句加别名  
	# """
	
		department;
	+------+--------------+
	| id   | name         |
	+------+--------------+
	|  200 | 技术         |
	|  201 | 人力资源     |
	|  202 | 销售         |
	|  203 | 运营         |
	+------+--------------+
	employee;
	+----+------------+--------+------+--------+
	| id | name       | sex    | age  | dep_id |
	+----+------------+--------+------+--------+
	|  1 | egon       | male   |   18 |    200 |  
	|  2 | alex       | female |   48 |    201 |  
	|  3 | wupeiqi    | male   |   38 |    201 |  
	|  4 | yuanhao    | female |   28 |    202 |  
	|  5 | liwenzhou  | male   |   18 |    200 |  
	|  6 | jingliyang | female |   18 |    204 |  
	+----+------------+--------+------+--------+


	# 一.找出平均年龄大于25岁以上的部门
	# (1) where
	select 
		d.id,d.name,avg(e.age)
	from 
		employee as e ,department as d
	where
		e.dep_id = d.id   #avg(e.age) 不可以用在where后  where后不能有小括号 avg_age
	group by 
		d.id,d.name   #各部门-group by
	having
		avg(e.age) > 25;   #avg(e.age) 可以用在having后   大于-having
		
	# mysql> select d.id from employee as e,department as d where e.dep_id=d.id group by d.id having avg(e.age) > 25;
# | id   | name         | avg(e.age) |
# +------+--------------+------------+
# |  201 | 人力资源     |    43.0000 |
# |  202 | 销售         |    28.0000
	
	# (2) inner join 
	select 
		d.id,d.name,avg(e.age)
	from 
		employee as e inner join department as d on e.dep_id = d.id
	group by 
		d.id,d.name
	having
		avg(e.age) > 25;
	# | id   | name         | avg(e.age) |
# +------+--------------+------------+
# |  201 | 人力资源     |    43.0000 |
# |  202 | 销售         |    28.0000
		
	department;
	+------+--------------+
	| id   | name         |
	+------+--------------+
	|  200 | 技术         |
	|  201 | 人力资源     |
	|  202 | 销售         |
	|  203 | 运营         |
	+------+--------------+
	employee;
	+----+------------+--------+------+--------+
	| id | name       | sex    | age  | dep_id |
	+----+------------+--------+------+--------+
	|  1 | egon       | male   |   18 |    200 |  
	|  2 | alex       | female |   48 |    201 |  
	|  3 | wupeiqi    | male   |   38 |    201 |  
	|  4 | yuanhao    | female |   28 |    202 |  
	|  5 | liwenzhou  | male   |   18 |    200 |  
	|  6 | jingliyang | female |   18 |    204 |  
	+----+------------+--------+------+--------+
		
	# 题目:找出平均年龄大于25岁的部门
	# (3) 子查询 
	# 1.先找出平均年龄大于25岁的部门id
	select dep_id from employee group by employee.dep_id having avg(age)>25; # 201 202
	# select 
		# dep_id 
	# from 
		# employee 
	# group by 
		# employee.dep_id 
	# having 
		# avg(age)>25; # 201 202
	
	# 2.通过部门的id找部门的名字
	select name from department where id in (201,202);
	
	# 3.综合拼接:
	select id , name from department where id in (select dep_id from employee group by employee.dep_id having avg(age)>25);
	# select 
		# id , name 
	# from 
		# department 
	# where 
		# id in (select 
					# dep_id 
				  # from 
					# employee 
				  # group by 
					# employee.dep_id 
				  # having 
					# avg(age)>25);

	# 二.查看技术部门员工姓名
	| id | name      | sex    | age  | dep_id | id   | name         |
	+----+-----------+--------+------+--------+------+--------------+
	|  1 | egon      | male   |   18 |    200 |  200 | 技术         |
	|  2 | alex      | female |   48 |    201 |  201 | 人力资源     |
	|  3 | wupeiqi   | male   |   38 |    201 |  201 | 人力资源     |
	|  4 | yuanhao   | female |   28 |    202 |  202 | 销售         |
	|  5 | liwenzhou | male   |   18 |    200 |  200 | 技术        

	# (1) 普通的where 查询
select 
	e.id,e.name
from
	employee as e,department as d
where
	e.dep_id = d.id
	and
	d.name = "技术"  #1 先连成一个大表，然后对大表进行单表条件查询（条件写在where后）
	
	# (2) inner join 
select 
	e.id,e.name
from
	employee as e 
	inner join department as d 
	on e.dep_id = d.id 
where
	d.name = "技术"
	
	# 题目 查看技术部门员工姓名
		department;
	+------+--------------+
	| id   | name         |
	+------+--------------+
	|  200 | 技术         |
	|  201 | 人力资源     |
	|  202 | 销售         |
	|  203 | 运营         |
	+------+--------------+
	employee;
	+----+------------+--------+------+--------+
	| id | name       | sex    | age  | dep_id |
	+----+------------+--------+------+--------+
	|  1 | egon       | male   |   18 |    200 |  
	|  2 | alex       | female |   48 |    201 |  
	|  3 | wupeiqi    | male   |   38 |    201 |  
	|  4 | yuanhao    | female |   28 |    202 |  
	|  5 | liwenzhou  | male   |   18 |    200 |  
	|  6 | jingliyang | female |   18 |    204 |  
	+----+------------+--------+------+--------+
	
	# (3)子查询
	# (1) 找技术部门对应的id
	select id from department where name = "技术";
	
	# (2) 通过id找员工姓名
	select name from employee where dep_id = 200;
	
	# (3) 综合拼接
	select id,name from employee where dep_id = (select id from department where name = "技术");
	# select 
		# id,name 
	# from 
		# employee 
	# where 
		# dep_id = (select 
						# id 
					# from 
						# department
					# where name = "技术");
	
	# 三.查看哪个部门没员工
	
	# 方法1:联表写法
	select
		d.id,d.name
	from
		department as d 
		left join employee as e 
		on d.id = e.dep_id
	where
		e.dep_id is null	 #这里null是关键字,不能用= 需要用is
		#1 先连成一个大表，然后对大表进行一次单表条件查询（条件写在where后）
	
	# 方法2:子查询 
	# 1.找员工在哪些部门 (200  201  202 204)
	select dep_id from employee  group by dep_id
	
	# 2.把不在该部门的员工找出来
	select  id  from department where id not in (200,201,202,204);  #不在 not in
	
	# 3.综合拼接
	select  id,name  from department where id not in (select dep_id from employee  group by dep_id);
	# select id,name  
	# from department 
	# where id not in (select dep_id 
					# from employee  
					# group by dep_id);
	
	department;
	+------+--------------+
	| id   | name         |
	+------+--------------+
	|  200 | 技术         |
	|  201 | 人力资源     |
	|  202 | 销售         |
	|  203 | 运营         |
	+------+--------------+
	employee;
	+----+------------+--------+------+--------+
	| id | name       | sex    | age  | dep_id |avg(age) 
	+----+------------+--------+------+--------+
	|  1 | egon       | male   |   18 |    200 |  28
	|  2 | alex       | female |   48 |    201 |  28
	|  3 | wupeiqi    | male   |   38 |    201 |  28
	|  4 | yuanhao    | female |   28 |    202 |  28
	|  5 | liwenzhou  | male   |   18 |    200 |  28
	|  6 | jingliyang | female |   18 |    204 |  28
	+----+------------+--------+------+--------+
	
	# 四.查询大于平均年龄的员工名与年龄
	# 方法1 子查询
	# 假设已经知道了平均年龄;
	select name,age from employee where age > 30;
	# 计算平均年龄
	select avg(age) from employee;  #这里的聚合函数avg没有用group by 分组
	# 综合拼接
	select name,age from employee where age > (select avg(age) from employee);  #子查询必须有小括号
	
	# 方法2  连表
	# 1计算平均年龄
	select avg(age) from employee;  #这里的聚合函数avg没有用group by 分组  注意
	| avg(age) |
	+----------+
	|  28.0000
	
	# 2 将平均年龄这个字段和表employee连表
	#   相当于给表employee新加了一个字段
	select 
		* 
	from
		employee as t1,(select avg(age) as avg_age from employee) as t2
	where and t1.age > t2.avg_age;  
	
	| id | name    | sex    | age  | dep_id | avg_age |
	+----+---------+--------+------+--------+---------+
	|  2 | alex    | female |   48 |    201 | 28.0000 |
	|  3 | wupeiqi | male   |   38 |    201 | 28.0000
	
	
	
		department;
	+------+--------------+
	| id   | name         |
	+------+--------------+
	|  200 | 技术         |
	|  201 | 人力资源     |
	|  202 | 销售         |
	|  203 | 运营         |
	+------+--------------+
	employee;
	+----+------------+--------+------+--------+
	| id | name       | sex    | age  | dep_id |avg(age) 
	+----+------------+--------+------+--------+
	|  1 | egon       | male   |   18 |    200 |  28
	|  2 | alex       | female |   48 |    201 |  28
	|  3 | wupeiqi    | male   |   38 |    201 |  28
	|  4 | yuanhao    | female |   28 |    202 |  28
	|  5 | liwenzhou  | male   |   18 |    200 |  28
	|  6 | jingliyang | female |   18 |    204 |  28
	+----+------------+--------+------+--------+
	
	# 五.把大于其本部门平均年龄的员工名和姓名查出来
	# 1.先计算本部门的平均年龄是多少
	select dep_id , avg(age) from employee  group by dep_id;	
	+--------+----------+
	| dep_id | avg(age) |
	+--------+----------+
	|    200 |  18.0000 |
	|    201 |  43.0000 |
	|    202 |  28.0000 |
	|    204 |  18.0000 |
	+--------+----------+

	# 2.把查询的各部门平均年龄和employee进行联表,变成一张大表,最后做单表查询
	select 
		*
	from
		employee as t1 inner join (1号查询出来的数据) as t2 on t1.dep_id = t2.dep_id
	
	# 3.综合拼装
select 
	*
from
	employee as t1 inner join (select dep_id , avg(age) as avg_age from employee  group by dep_id) as t2 on t1.dep_id = t2.dep_id
	| id | name       | sex    | age  | dep_id | dep_id | avg(age) |
	+----+------------+--------+------+--------+--------+----------+
	|  1 | egon       | male   |   18 |    200 |    200 |  18.0000 |
	|  2 | alex       | female |   48 |    201 |    201 |  43.0000 |
	|  3 | wupeiqi    | male   |   38 |    201 |    201 |  43.0000 |
	|  4 | yuanhao    | female |   28 |    202 |    202 |  28.0000 |
	|  5 | liwenzhou  | male   |   18 |    200 |    200 |  18.0000 |
	|  6 | jingliyang | female |   18 |    204 |    204 |  18.0000 |
	
# select 	*
# from employee as t1 
	# inner join (select dep_id , avg(age) as avg_age 
				# from employee  
				# group by dep_id) 
	# as t2 on t1.dep_id = t2.dep_id

	
	# 4.最后做一次单表查询,让age > 平均值	
select 
	*
from
	employee as t1 inner join (select dep_id , avg(age) as avg_age from employee  group by dep_id) as t2 on t1.dep_id = t2.dep_id
where 
	age >avg_age  #注意点:avg(age)中的()不能写在where后面,需要别名才行
	
# select 	*
# from employee as t1 
	# inner join (select dep_id , avg(age) as avg_age 
				# from employee  
				# group by dep_id) as t2 
	# on t1.dep_id = t2.dep_id
# where age >avg_age  #注意点:avg(age)中的()不能写在where后面,需要别名才行
	
	
	# 六.查询每个部门最新入职的那位员工  # 利用上一套数据表进行查询;
	employee
	+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
	| id | emp_name   | sex    | age | hire_date  | post                                    | post_comment | salary     | office | depart_id |    max_date
	+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
	|  1 | egon       | male   |  18 | 2017-03-01 | 老男孩驻沙河办事处外交大使              |              |    7300.33 |    401 |         1 | 2017-03-01
	|  2 | alex       | male   |  78 | 2015-03-02 | teacher                                 | NULL         | 1000000.31 |    401 |         1 | 2015-03-02
	|  3 | wupeiqi    | male   |  81 | 2013-03-05 | teacher                                 | NULL         |    8300.00 |    401 |         1 | 2015-03-02 
	|  4 | yuanhao    | male   |  73 | 2014-07-01 | teacher                                 | NULL         |    3500.00 |    401 |         1 | 2015-03-02
	|  5 | liwenzhou  | male   |  28 | 2012-11-01 | teacher                                 | NULL         |    2100.00 |    401 |         1 | 2015-03-02
	|  6 | jingliyang | female |  18 | 2011-02-11 | teacher                                 | NULL         |    9000.00 |    401 |         1 | 2015-03-02
	|  7 | jinxin     | male   |  18 | 1900-03-01 | teacher                                 | NULL         |   30000.00 |    401 |         1 | 2015-03-02
	|  8 | 成龙       | male   |  48 | 2010-11-11 | teacher                                 | NULL         |   10000.00 |    401 |         1 | 2015-03-02
	|  9 | 歪歪       | female |  48 | 2015-03-11 | sale                                    | NULL         |    3000.13 |    402 |         2 | 2017-01-27
	| 10 | 丫丫       | female |  38 | 2010-11-01 | sale                                    | NULL         |    2000.35 |    402 |         2 | 2017-01-27
	| 11 | 丁丁       | female |  18 | 2011-03-12 | sale                                    | NULL         |    1000.37 |    402 |         2 | 2017-01-27
	| 12 | 星星       | female |  18 | 2016-05-13 | sale                                    | NULL         |    3000.29 |    402 |         2 | 2017-01-27
	| 13 | 格格       | female |  28 | 2017-01-27 | sale                                    | NULL         |    4000.33 |    402 |         2 | 2017-01-27
	| 14 | 张野       | male   |  28 | 2016-03-11 | operation                               | NULL         |   10000.13 |    403 |         3 | 2016-03-11
	| 15 | 程咬金     | male   |  18 | 1997-03-12 | operation                               | NULL         |   20000.00 |    403 |         3 | 2016-03-11
	| 16 | 程咬银     | female |  18 | 2013-03-11 | operation                               | NULL         |   19000.00 |    403 |         3 | 2016-03-11
	| 17 | 程咬铜     | male   |  18 | 2015-04-11 | operation                               | NULL         |   18000.00 |    403 |         3 | 2016-03-11
	| 18 | 程咬铁     | female |  18 | 2014-05-12 | operation                               | NULL         |   17000.00 |    403 |         3 | 2016-03-11
	+----+------------+--------+-----+------------+-----------------------------------------+--------------+------------+--------+-----------+
	
	# 1.找各部门的最新入职的时间
	select post,max(hire_date) as max_date from employee group by post;
	
	+-----------------------------------------+------------+
	| post                                    | max_date   |
	+-----------------------------------------+------------+
	| operation                               | 2016-03-11 |
	| sale                                    | 2017-01-27 |
	| teacher                                 | 2015-03-02 |
	| 老男孩驻沙河办事处外交大使             | 2017-03-01 |
	+-----------------------------------------+------------+
	
	# 2.把子查询搜索出来的结果作为一张表和employee这个表做联表,把max_date拼接在employee这个表中,变成一张大表,最后做一次单表查询
	select 
		*
	from
		employee as t1 inner join (1号数据) as t2 on t1.post = t2.post
	where
		t1.hire_date = t2.max_date
		
	# 3.综合拼装
# 方式1  inner join on
select 
	emp_name , max_date
from
	employee as t1 inner join (select post,max(hire_date) as max_date from employee group by post) as t2 on t1.post = t2.post
where
	t1.hire_date = t2.max_date;   #注意点:max(hire_date)中的()不能写在where后面,需要别名才行   #连大表后,where加一个条件(大表单表查询)
	
# select 	emp_name , max_date
# from	employee as t1 
	# inner join (select post,max(hire_date) as max_date 
				# from employee 
				# group by post) as t2 
	# on t1.post = t2.post
# where	t1.hire_date = t2.max_date

# 方式2  where
select 
	emp_name , max_date
from
	employee as t1, (select post,max(hire_date) as max_date from employee group by post) as t2 
where t1.post = t2.post 
      and t1.hire_date = t2.max_date; 
	
	# 七.带EXISTS关键字的子查询
	# """
	# exists 关键字 , 表达存在 , 应用在子查询中
		# 如果内层sql , 能够查到数据, 返回True ,  外层sql执行相应的sql语句
		# 如果内层sql , 不能查到数据, 返回False , 外层sql不执行sql语句
	# """
	select * from employee where exists (select * from employee where id = 1);
	select * from employee where exists (select * from employee where id = 100000);
	# mysql> select * from employee where exists (select * from employee where id = 1000);
# Empty set (0.00 sec)

	
	
	# """
	# 总结: 
		# 子查询可以单独作为临时数据,作为一张表或者一个字段,通过()进行包裹,表达一个整体;
		# 一般用在from,where,select.子句的后面
		# 可以通过查询出来的数据和另外的表做联表变成更大一张表,
		# 最后做单表查询-where条件,达到目的;
	# """
	
	
	





















	
	
	
	
	
	
	
	