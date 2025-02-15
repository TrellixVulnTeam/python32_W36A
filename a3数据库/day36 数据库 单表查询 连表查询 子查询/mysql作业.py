# [mysql周末作业]
### 1.表结构:
![表结构](assets/表结构.png)
### 2.黏贴如下sql,直接建表
```
# 1、创建表
# 创建班级表
create table class(
cid int primary key auto_increment,
caption varchar(32) not null
);

# 创建学生表
create table student(
sid int primary key auto_increment,
gender char(1) not null,
class_id int not null,
sname varchar(32) not null,
foreign key(class_id) references class(cid) on delete cascade on update cascade
);

# 创建老师表
create table teacher(
tid int primary key auto_increment,
tname varchar(32) not null
);

# 创建课程表
create table course(
cid int primary key auto_increment,
cname varchar(32) not null,
teacher_id int not null,
foreign key(teacher_id) references teacher(tid) on delete cascade on update cascade
);

# 创建成绩表
create table score(
sid int primary key auto_increment,
student_id int not null,
course_id int not null,
num int not null,
foreign key(student_id) references student(sid) on delete cascade on update cascade,
foreign key(course_id) references course(cid) on delete cascade on update cascade
);


# 2、插入记录
# 班级表插入记录
insert into class values
('1', '三年二班'), 
('2', '三年三班'), 
('3', '一年二班'), 
('4', '二年一班');

# 学生表插入记录
insert into student values
('1', '男', '1', '理解'), 
('2', '女', '1', '钢蛋'), 
('3', '男', '1', '张三'), 
('4', '男', '1', '张一'), 
('5', '女', '1', '张二'), 
('6', '男', '1', '张四'), 
('7', '女', '2', '铁锤'),
('8', '男', '2', '李三'), 
('9', '男', '2', '李一'), 
('10', '女', '2', '李二'), 
('11', '男', '2', '李四'), 
('12', '女', '3', '如花'), 
('13', '男', '3', '刘三'), 
('14', '男', '3', '刘一'), 
('15', '女', '3', '刘二'), 
('16', '男', '3', '刘四');

# 老师表插入记录
insert into teacher values
('1', '张磊'), 
('2', '李平'), 
('3', '刘海燕'), 
('4', '朱云海'), 
('5', '李春秋');

# 课程表插入记录
insert into course values
('1', '生物', '1'), 
('2', '物理', '2'), 
('3', '体育', '3'), 
('4', '美术', '2');

# 成绩表插入记录
insert into score values
('1', '1', '1', '10'), 
('2', '1', '2', '9'), 
('3', '1', '3', '76'),
('5', '1', '4', '66'), 
('6', '2', '1', '8'), 
('8', '2', '3', '68'), 
('9', '2', '4', '99'), 
('10', '3', '1', '77'), 
('11', '3', '2', '66'), 
('12', '3', '3', '87'), 
('13', '3', '4', '99'), 
('14', '4', '1', '79'), 
('15', '4', '2', '11'), 
('16', '4', '3', '67'), 
('17', '4', '4', '100'), 
('18', '5', '1', '79'), 
('19', '5', '2', '11'), 
('20', '5', '3', '67'), 
('21', '5', '4', '100'), 
('22', '6', '1', '9'), 
('23', '6', '2', '100'), 
('24', '6', '3', '67'), 
('25', '6', '4', '100'), 
('26', '7', '1', '9'), 
('27', '7', '2', '100'), 
('28', '7', '3', '67'), 
('29', '7', '4', '88'), 
('30', '8', '1', '9'), 
('31', '8', '2', '100'), 
('32', '8', '3', '67'),
('33', '8', '4', '88'), 
('34', '9', '1', '91'), 
('35', '9', '2', '88'), 
('36', '9', '3', '67'), 
('37', '9', '4', '22'), 
('38', '10', '1', '90'), 
('39', '10', '2', '77'), 
('40', '10', '3', '43'), 
('41', '10', '4', '87'), 
('42', '11', '1', '90'), 
('43', '11', '2', '77'), 
('44', '11', '3', '43'), 
('45', '11', '4', '87'), 
('46', '12', '1', '90'), 
('47', '12', '2', '77'), 
('48', '12', '3', '43'), 
('49', '12', '4', '87'), 
('52', '13', '3', '87');
```
### 3.练习题目

```
1、查询所有的课程的名称以及对应的任课老师姓名
select 
	*
from course as c,teacher as t
where  c.teacher_id = t.tid;

| cid | cname  | teacher_id | tid | tname     |
+-----+--------+------------+-----+-----------+
|   1 | 生物   |          1 |   1 | 张磊      |
|   2 | 物理   |          2 |   2 | 李平      |
|   3 | 体育   |          3 |   3 | 刘海燕    |
|   4 | 美术   |          2 |   2 | 李平 

select 
	cname,tname
from course as c,teacher as t
where  c.teacher_id = t.tid;

| cname  | tname     |
+--------+-----------+
| 生物   | 张磊      |
| 物理   | 李平      |
| 体育   | 刘海燕    |
| 美术   | 李平  

2、查询学生表中男女生各有多少人
select * from student;

select gender,count(*) from student group by gender;
# | gender | count(*) |
# +--------+----------+
# | 女     |        6 |
# | 男     |       10 

3、查询物理成绩等于100的学生的姓名
select
	t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t3.num = 100
	and t2.cname = '物理';

| sname  | cname  | num |
+--------+--------+-----+
| 张四   | 物理   | 100 |
| 铁锤   | 物理   | 100 |
| 李三   | 物理   | 100 |


4、查询平均成绩大于八十分的同学的姓名和平均成绩
# 1 查询每个同学的平均成绩
select
	t1.sid,t1.sname,avg(num) as avg_num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
group by t1.sid,t1.sname;

| sid | sname  | avg_num |
+-----+--------+---------+
|   1 | 理解   | 40.2500 |
|   2 | 钢蛋   | 58.3333 |
|   3 | 张三   | 82.2500 |
|   4 | 张一   | 64.2500 |
|   5 | 张二   | 64.2500 |
|   6 | 张四   | 69.0000 |
|   7 | 铁锤   | 66.0000 |
|   8 | 李三   | 66.0000 |
|   9 | 李一   | 67.0000 |
|  10 | 李二   | 74.2500 |
|  11 | 李四   | 74.2500 |
|  12 | 如花   | 74.2500 |
|  13 | 刘三   | 87.0000 |


select avg_num from t1 wherer avg_num > 80;


select t1.sname,t1.avg_num from (select
	t1.sid,t1.sname,avg(num) as avg_num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
group by t1.sid,t1.sname) as t1 where t1.avg_num > 80;
| sname  | avg_num |
+--------+---------+
| 张三   | 82.2500 |
| 刘三   | 87.0000 

# select avg_num from (select
	# t1.sid,t1.sname,avg(num) as avg_num
# from 
	# student as t1,course as t2,score as t3
# where 
	# t3.student_id = t1.sid and t3.course_id = t2.cid
# group by t1.sid,t1.sname)  where avg_num > 80;
# Every derived table must have its own alias


5、查询所有学生的学号，姓名，选课数，总成绩

select
	t1.sid,t1.sname,count(t2.cid),sum(t3.num)
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
group by 
	t1.sid,t1.sname;
	
| sid | sname  | count(t2.cid) | sum(t3.num) |
+-----+--------+---------------+-------------+
|   1 | 理解   |             4 |         161 |
|   2 | 钢蛋   |             3 |         175 |
|   3 | 张三   |             4 |         329 |
|   4 | 张一   |             4 |         257 |
|   5 | 张二   |             4 |         257 |
|   6 | 张四   |             4 |         276 |
|   7 | 铁锤   |             4 |         264 |
|   8 | 李三   |             4 |         264 |
|   9 | 李一   |             4 |         268 |
|  10 | 李二   |             4 |         297 |
|  11 | 李四   |             4 |         297 |
|  12 | 如花   |             4 |         297 |
|  13 | 刘三   |             1 |          87

6、 查询姓李老师的个数
select count(*) from teacher where tname like '李%';

# | count(*) |
# +----------+
# |        2 |

7、 查询没有报李平老师课的学生姓名
select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid;
	
select
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid;

# 1 所有报课学生的sid
| sid |
+-----+
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|  13 |

select
	*
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
select
	distinct(t1.sid)
from 
	student as t1,course as t2,score as t3,teacher as t4
where 
	t3.student_id = t1.sid 
	and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
# # 2 所有报李平老师课学生的sid
| sid |
+-----+
|   1 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|   2 |

select 
	*
from 
		(select
		distinct(t1.sid),t1.sname
	from 
		student as t1,course as t2,score as t3,teacher as t4
	where 
		t3.student_id = t1.sid 
		and t3.course_id = t2.cid
	and t2.teacher_id = t4.tid) as t1 left join (select
		distinct(t1.sid)
	from 
		student as t1,course as t2,score as t3,teacher as t4
	where 
		t3.student_id = t1.sid 
		and t3.course_id = t2.cid
		and t2.teacher_id = t4.tid
		and t4.tname = '李平') as t2 on t1.sid = t2.sid;

# 3报课的学生中,没有报李平老师可的同学  --刘三
| sid | sname  | sid  |
+-----+--------+------+
|   1 | 理解   |    1 |
|   2 | 钢蛋   |    2 |
|   3 | 张三   |    3 |
|   4 | 张一   |    4 |
|   5 | 张二   |    5 |
|   6 | 张四   |    6 |
|   7 | 铁锤   |    7 |
|   8 | 李三   |    8 |
|   9 | 李一   |    9 |
|  10 | 李二   |   10 |
|  11 | 李四   |   11 |
|  12 | 如花   |   12 |
|  13 | 刘三   | NULL |   

select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	
select 
	*
from 
	student as t1 left join t2 on t1.sid = t2.sid;

select 
	t1.sid,t1.sname,t2.num
from 
	student as t1 left join (select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid) as t2 on t1.sid = t2.sid;

# 4没报课的学生(一门课都没报),  --刘一 刘二 刘四
# 这个前3步是内连接,看不出来,第4步,用student当主表 左连接才能看到
| sid | sname  | num  |
+-----+--------+------+
|   1 | 理解   |   10 |
|   1 | 理解   |    9 |
|   1 | 理解   |   76 |
|   1 | 理解   |   66 |
|   2 | 钢蛋   |    8 |
|   2 | 钢蛋   |   68 |
|   2 | 钢蛋   |   99 |
|   3 | 张三   |   77 |
|   3 | 张三   |   66 |
|   3 | 张三   |   87 |
|   3 | 张三   |   99 |
|   4 | 张一   |   79 |
|   4 | 张一   |   11 |
|   4 | 张一   |   67 |
|   4 | 张一   |  100 |
|   5 | 张二   |   79 |
|   5 | 张二   |   11 |
|   5 | 张二   |   67 |
|   5 | 张二   |  100 |
|   6 | 张四   |    9 |
|   6 | 张四   |  100 |
|   6 | 张四   |   67 |
|   6 | 张四   |  100 |
|   7 | 铁锤   |    9 |
|   7 | 铁锤   |  100 |
|   7 | 铁锤   |   67 |
|   7 | 铁锤   |   88 |
|   8 | 李三   |    9 |
|   8 | 李三   |  100 |
|   8 | 李三   |   67 |
|   8 | 李三   |   88 |
|   9 | 李一   |   91 |
|   9 | 李一   |   88 |
|   9 | 李一   |   67 |
|   9 | 李一   |   22 |
|  10 | 李二   |   90 |
|  10 | 李二   |   77 |
|  10 | 李二   |   43 |
|  10 | 李二   |   87 |
|  11 | 李四   |   90 |
|  11 | 李四   |   77 |
|  11 | 李四   |   43 |
|  11 | 李四   |   87 |
|  12 | 如花   |   90 |
|  12 | 如花   |   77 |
|  12 | 如花   |   43 |
|  12 | 如花   |   87 |
|  13 | 刘三   |   87 |
|  14 | 刘一   | NULL |
|  15 | 刘二   | NULL |
|  16 | 刘四   | NULL |
	

8、 查询物理课程的分数比生物课程的分数高的学生的学号
select
	t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid;
	
| sname  | cname  | num |
+--------+--------+-----+
| 理解   | 生物   |  10 |
| 钢蛋   | 生物   |   8 |
| 张三   | 生物   |  77 |
| 张一   | 生物   |  79 |
| 张二   | 生物   |  79 |
| 张四   | 生物   |   9 |
| 铁锤   | 生物   |   9 |
| 李三   | 生物   |   9 |
| 李一   | 生物   |  91 |
| 李二   | 生物   |  90 |
| 李四   | 生物   |  90 |
| 如花   | 生物   |  90 |
| 理解   | 物理   |   9 |
| 张三   | 物理   |  66 |
| 张一   | 物理   |  11 |
| 张二   | 物理   |  11 |
| 张四   | 物理   | 100 |
| 铁锤   | 物理   | 100 |
| 李三   | 物理   | 100 |
| 李一   | 物理   |  88 |
| 李二   | 物理   |  77 |
| 李四   | 物理   |  77 |
| 如花   | 物理   |  77 |


select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理';
	
| sid | sname  | cname  | num |
+-----+--------+--------+-----+
|   1 | 理解   | 物理   |   9 |
|   3 | 张三   | 物理   |  66 |
|   4 | 张一   | 物理   |  11 |
|   5 | 张二   | 物理   |  11 |
|   6 | 张四   | 物理   | 100 |
|   7 | 铁锤   | 物理   | 100 |
|   8 | 李三   | 物理   | 100 |
|   9 | 李一   | 物理   |  88 |
|  10 | 李二   | 物理   |  77 |
|  11 | 李四   | 物理   |  77 |
|  12 | 如花   | 物理   |  77 |

	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '生物';
	
| sid | sname  | cname  | num |
+-----+--------+--------+-----+
|   1 | 理解   | 生物   |  10 |
|   2 | 钢蛋   | 生物   |   8 |
|   3 | 张三   | 生物   |  77 |
|   4 | 张一   | 生物   |  79 |
|   5 | 张二   | 生物   |  79 |
|   6 | 张四   | 生物   |   9 |
|   7 | 铁锤   | 生物   |   9 |
|   8 | 李三   | 生物   |   9 |
|   9 | 李一   | 生物   |  91 |
|  10 | 李二   | 生物   |  90 |
|  11 | 李四   | 生物   |  90 |
|  12 | 如花   | 生物   |  90 |

select 
	*
from 
	(select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理')as t1,(select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '生物') as t2
where t1.sid = t2.sid;

| sid | sname  | cname  | num | sid | sname  | cname  | num |
+-----+--------+--------+-----+-----+--------+--------+-----+
|   1 | 理解   | 物理   |   9 |   1 | 理解   | 生物   |  10 |
|   3 | 张三   | 物理   |  66 |   3 | 张三   | 生物   |  77 |
|   4 | 张一   | 物理   |  11 |   4 | 张一   | 生物   |  79 |
|   5 | 张二   | 物理   |  11 |   5 | 张二   | 生物   |  79 |
|   6 | 张四   | 物理   | 100 |   6 | 张四   | 生物   |   9 |
|   7 | 铁锤   | 物理   | 100 |   7 | 铁锤   | 生物   |   9 |
|   8 | 李三   | 物理   | 100 |   8 | 李三   | 生物   |   9 |
|   9 | 李一   | 物理   |  88 |   9 | 李一   | 生物   |  91 |
|  10 | 李二   | 物理   |  77 |  10 | 李二   | 生物   |  90 |
|  11 | 李四   | 物理   |  77 |  11 | 李四   | 生物   |  90 |
|  12 | 如花   | 物理   |  77 |  12 | 如花   | 生物   |  90 |


select 
	*
from 
	(select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理')as t1,(select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '生物') as t2
where t1.sid = t2.sid and t1.num > t2.num;
| sid | sname  | cname  | num | sid | sname  | cname  | num |
+-----+--------+--------+-----+-----+--------+--------+-----+
|   6 | 张四   | 物理   | 100 |   6 | 张四   | 生物   |   9 |
|   7 | 铁锤   | 物理   | 100 |   7 | 铁锤   | 生物   |   9 |
|   8 | 李三   | 物理   | 100 |   8 | 李三   | 生物   |   9 |

# 查询物理课程的分数比生物课程的分数高的学生的学号

9、 查询没有同时选修物理课程和体育课程的学生姓名
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid;
	
| sname  | cname  | num |
+--------+--------+-----+
| 理解   | 生物   |  10 |
| 钢蛋   | 生物   |   8 |
| 张三   | 生物   |  77 |
| 张一   | 生物   |  79 |
| 张二   | 生物   |  79 |
| 张四   | 生物   |   9 |
| 铁锤   | 生物   |   9 |
| 李三   | 生物   |   9 |
| 李一   | 生物   |  91 |
| 李二   | 生物   |  90 |
| 李四   | 生物   |  90 |
| 如花   | 生物   |  90 |
| 理解   | 物理   |   9 |
| 张三   | 物理   |  66 |
| 张一   | 物理   |  11 |
| 张二   | 物理   |  11 |
| 张四   | 物理   | 100 |
| 铁锤   | 物理   | 100 |
| 李三   | 物理   | 100 |
| 李一   | 物理   |  88 |
| 李二   | 物理   |  77 |
| 李四   | 物理   |  77 |
| 如花   | 物理   |  77 |

select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理';
	
| sname  | cname  | num |
+--------+--------+-----+
| 理解   | 物理   |   9 |
| 张三   | 物理   |  66 |
| 张一   | 物理   |  11 |
| 张二   | 物理   |  11 |
| 张四   | 物理   | 100 |
| 铁锤   | 物理   | 100 |
| 李三   | 物理   | 100 |
| 李一   | 物理   |  88 |
| 李二   | 物理   |  77 |
| 李四   | 物理   |  77 |
| 如花   | 物理   |  77 |

select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '体育';
	
| sname  | cname  | num |
+--------+--------+-----+
| 理解   | 体育   |  76 |
| 钢蛋   | 体育   |  68 |
| 张三   | 体育   |  87 |
| 张一   | 体育   |  67 |
| 张二   | 体育   |  67 |
| 张四   | 体育   |  67 |
| 铁锤   | 体育   |  67 |
| 李三   | 体育   |  67 |
| 李一   | 体育   |  67 |
| 李二   | 体育   |  43 |
| 李四   | 体育   |  43 |
| 如花   | 体育   |  43 |
| 刘三   | 体育   |  87 |

# 查询没有同时选修物理课程和体育课程的学生姓名

#001同时选修物理课程和体育课程的学生姓名
select 
	*
from 
		(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname = '物理') as t1,(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname = '体育') as t2
where t1.sid = t2.sid;

| sid | sname  | cname  | num | sid | sname  | cname  | num |
+-----+--------+--------+-----+-----+--------+--------+-----+
|   1 | 理解   | 物理   |   9 |   1 | 理解   | 体育   |  76 |
|   3 | 张三   | 物理   |  66 |   3 | 张三   | 体育   |  87 |
|   4 | 张一   | 物理   |  11 |   4 | 张一   | 体育   |  67 |
|   5 | 张二   | 物理   |  11 |   5 | 张二   | 体育   |  67 |
|   6 | 张四   | 物理   | 100 |   6 | 张四   | 体育   |  67 |
|   7 | 铁锤   | 物理   | 100 |   7 | 铁锤   | 体育   |  67 |
|   8 | 李三   | 物理   | 100 |   8 | 李三   | 体育   |  67 |
|   9 | 李一   | 物理   |  88 |   9 | 李一   | 体育   |  67 |
|  10 | 李二   | 物理   |  77 |  10 | 李二   | 体育   |  43 |
|  11 | 李四   | 物理   |  77 |  11 | 李四   | 体育   |  43 |
|  12 | 如花   | 物理   |  77 |  12 | 如花   | 体育   |  43 

#报了物理课的同学,减去物理和体育2个课都报了的同学
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '物理' and t1.sid not in (select 
		t1.sid
	from 
			(select
			t1.sid,t1.sname,t2.cname,t3.num
		from 
			student as t1,course as t2,score as t3
		where 
			t3.student_id = t1.sid and t3.course_id = t2.cid
			and t2.cname = '物理') as t1,(select
			t1.sid,t1.sname,t2.cname,t3.num
		from 
			student as t1,course as t2,score as t3
		where 
			t3.student_id = t1.sid and t3.course_id = t2.cid
			and t2.cname = '体育') as t2
	where t1.sid = t2.sid);

#报了体育课的同学,减去物理和体育2个课都报了的同学	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t2.cname = '体育' and t1.sid not in (select 
		t1.sid
	from 
			(select
			t1.sid,t1.sname,t2.cname,t3.num
		from 
			student as t1,course as t2,score as t3
		where 
			t3.student_id = t1.sid and t3.course_id = t2.cid
			and t2.cname = '物理') as t1,(select
			t1.sid,t1.sname,t2.cname,t3.num
		from 
			student as t1,course as t2,score as t3
		where 
			t3.student_id = t1.sid and t3.course_id = t2.cid
			and t2.cname = '体育') as t2
	where t1.sid = t2.sid);
| sid | sname  | cname  | num |
+-----+--------+--------+-----+
|   2 | 钢蛋   | 体育   |  68 |
|  13 | 刘三   | 体育   |  87


10、查询挂科超过两门(包括两门)的学生姓名和班级
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid;
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t3.num<60;
| sid | sname  | cname  | num |
+-----+--------+--------+-----+
|   1 | 理解   | 生物   |  10 |
|   1 | 理解   | 物理   |   9 |
|   2 | 钢蛋   | 生物   |   8 |
|   4 | 张一   | 物理   |  11 |
|   5 | 张二   | 物理   |  11 |
|   6 | 张四   | 生物   |   9 |
|   7 | 铁锤   | 生物   |   9 |
|   8 | 李三   | 生物   |   9 |
|   9 | 李一   | 美术   |  22 |
|  10 | 李二   | 体育   |  43 |
|  11 | 李四   | 体育   |  43 |
|  12 | 如花   | 体育   |  43 |

select t1.sid,t1.sname,count(*) from (select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and t3.num<60) as t1 group by t1.sid,t1.sname;
	
| sid | sname  | count(*) |
+-----+--------+----------+
|   1 | 理解   |        2 |
|   2 | 钢蛋   |        1 |
|   4 | 张一   |        1 |
|   5 | 张二   |        1 |
|   6 | 张四   |        1 |
|   7 | 铁锤   |        1 |
|   8 | 李三   |        1 |
|   9 | 李一   |        1 |
|  10 | 李二   |        1 |
|  11 | 李四   |        1 |
|  12 | 如花   |        1 

select
t1.sname,t2.caption
from
student as t1,class as t2
where t1.class_id = t2.cid;

| sid | gender | class_id | sname  | cid | caption      |
+-----+--------+----------+--------+-----+--------------+
|   1 | 男     |        1 | 理解   |   1 | 三年二班     |
|   2 | 女     |        1 | 钢蛋   |   1 | 三年二班     |
|   3 | 男     |        1 | 张三   |   1 | 三年二班     |
|   4 | 男     |        1 | 张一   |   1 | 三年二班     |
|   5 | 女     |        1 | 张二   |   1 | 三年二班     |
|   6 | 男     |        1 | 张四   |   1 | 三年二班     |
|   7 | 女     |        2 | 铁锤   |   2 | 三年三班     |
|   8 | 男     |        2 | 李三   |   2 | 三年三班     |
|   9 | 男     |        2 | 李一   |   2 | 三年三班     |
|  10 | 女     |        2 | 李二   |   2 | 三年三班     |
|  11 | 男     |        2 | 李四   |   2 | 三年三班     |
|  12 | 女     |        3 | 如花   |   3 | 一年二班     |
|  13 | 男     |        3 | 刘三   |   3 | 一年二班     |
|  14 | 男     |        3 | 刘一   |   3 | 一年二班     |
|  15 | 女     |        3 | 刘二   |   3 | 一年二班     |
|  16 | 男     |        3 | 刘四   |   3 | 一年二班  

select
t1.sname,t2.caption
from
student as t1,class as t2
where t1.class_id = t2.cid and t1.sname = '理解';

| sname  | caption      |
+--------+--------------+
| 理解   | 三年二班


11、查询选修了所有课程的学生姓名
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid;
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and cname='生物';
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and cname='物理';
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and cname='体育';
	
select
	t1.sid,t1.sname,t2.cname,t3.num
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	and cname='美术';
	
select 
	*
from (select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and cname='生物') as t1,(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and cname='物理') as t2,(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and cname='体育') as t3,(select
		t1.sid,t1.sname,t2.cname,t3.num
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and cname='美术') as t4
where t1.sid = t2.sid and t2.sid = t3.sid and t3.sid = t4.sid;

| sid | sname  | cname  | num | sid | sname  | cname  | num | sid | sname  | cname  | num | sid | sname  | cname  | num |
+-----+--------+--------+-----+-----+--------+--------+-----+-----+--------+--------+-----+-----+--------+--------+-----+
|   1 | 理解   | 生物   |  10 |   1 | 理解   | 物理   |   9 |   1 | 理解   | 体育   |  76 |   1 | 理解   | 美术   |  66 |
|   3 | 张三   | 生物   |  77 |   3 | 张三   | 物理   |  66 |   3 | 张三   | 体育   |  87 |   3 | 张三   | 美术   |  99 |
|   4 | 张一   | 生物   |  79 |   4 | 张一   | 物理   |  11 |   4 | 张一   | 体育   |  67 |   4 | 张一   | 美术   | 100 |
|   5 | 张二   | 生物   |  79 |   5 | 张二   | 物理   |  11 |   5 | 张二   | 体育   |  67 |   5 | 张二   | 美术   | 100 |
|   6 | 张四   | 生物   |   9 |   6 | 张四   | 物理   | 100 |   6 | 张四   | 体育   |  67 |   6 | 张四   | 美术   | 100 |
|   7 | 铁锤   | 生物   |   9 |   7 | 铁锤   | 物理   | 100 |   7 | 铁锤   | 体育   |  67 |   7 | 铁锤   | 美术   |  88 |
|   8 | 李三   | 生物   |   9 |   8 | 李三   | 物理   | 100 |   8 | 李三   | 体育   |  67 |   8 | 李三   | 美术   |  88 |
|   9 | 李一   | 生物   |  91 |   9 | 李一   | 物理   |  88 |   9 | 李一   | 体育   |  67 |   9 | 李一   | 美术   |  22 |
|  10 | 李二   | 生物   |  90 |  10 | 李二   | 物理   |  77 |  10 | 李二   | 体育   |  43 |  10 | 李二   | 美术   |  87 |
|  11 | 李四   | 生物   |  90 |  11 | 李四   | 物理   |  77 |  11 | 李四   | 体育   |  43 |  11 | 李四   | 美术   |  87 |
|  12 | 如花   | 生物   |  90 |  12 | 如花   | 物理   |  77 |  12 | 如花   | 体育   |  43 |  12 | 如花   | 美术   |  87


12、查询李平老师教的课程的所有成绩记录
select
	*
from 
	course as t2,score as t3,teacher as t4
where 
	t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
| cid | cname  | teacher_id | sid | student_id | course_id | num | tid | tname  |
+-----+--------+------------+-----+------------+-----------+-----+-----+--------+
|   2 | 物理   |          2 |   2 |          1 |         2 |   9 |   2 | 李平   |
|   2 | 物理   |          2 |  11 |          3 |         2 |  66 |   2 | 李平   |
|   2 | 物理   |          2 |  15 |          4 |         2 |  11 |   2 | 李平   |
|   2 | 物理   |          2 |  19 |          5 |         2 |  11 |   2 | 李平   |
|   2 | 物理   |          2 |  23 |          6 |         2 | 100 |   2 | 李平   |
|   2 | 物理   |          2 |  27 |          7 |         2 | 100 |   2 | 李平   |
|   2 | 物理   |          2 |  31 |          8 |         2 | 100 |   2 | 李平   |
|   2 | 物理   |          2 |  35 |          9 |         2 |  88 |   2 | 李平   |
|   2 | 物理   |          2 |  39 |         10 |         2 |  77 |   2 | 李平   |
|   2 | 物理   |          2 |  43 |         11 |         2 |  77 |   2 | 李平   |
|   2 | 物理   |          2 |  47 |         12 |         2 |  77 |   2 | 李平   |
|   4 | 美术   |          2 |   5 |          1 |         4 |  66 |   2 | 李平   |
|   4 | 美术   |          2 |   9 |          2 |         4 |  99 |   2 | 李平   |
|   4 | 美术   |          2 |  13 |          3 |         4 |  99 |   2 | 李平   |
|   4 | 美术   |          2 |  17 |          4 |         4 | 100 |   2 | 李平   |
|   4 | 美术   |          2 |  21 |          5 |         4 | 100 |   2 | 李平   |
|   4 | 美术   |          2 |  25 |          6 |         4 | 100 |   2 | 李平   |
|   4 | 美术   |          2 |  29 |          7 |         4 |  88 |   2 | 李平   |
|   4 | 美术   |          2 |  33 |          8 |         4 |  88 |   2 | 李平   |
|   4 | 美术   |          2 |  37 |          9 |         4 |  22 |   2 | 李平   |
|   4 | 美术   |          2 |  41 |         10 |         4 |  87 |   2 | 李平   |
|   4 | 美术   |          2 |  45 |         11 |         4 |  87 |   2 | 李平   |
|   4 | 美术   |          2 |  49 |         12 |         4 |  87 |   2 | 李平 


select
	t2.cname,t3.num,t4.tname
from 
	course as t2,score as t3,teacher as t4
where 
	t3.course_id = t2.cid
	and t2.teacher_id = t4.tid
	and t4.tname = '李平';
	
| cname  | num | tname  |
+--------+-----+--------+
| 物理   |   9 | 李平   |
| 物理   |  66 | 李平   |
| 物理   |  11 | 李平   |
| 物理   |  11 | 李平   |
| 物理   | 100 | 李平   |
| 物理   | 100 | 李平   |
| 物理   | 100 | 李平   |
| 物理   |  88 | 李平   |
| 物理   |  77 | 李平   |
| 物理   |  77 | 李平   |
| 物理   |  77 | 李平   |
| 美术   |  66 | 李平   |
| 美术   |  99 | 李平   |
| 美术   |  99 | 李平   |
| 美术   | 100 | 李平   |
| 美术   | 100 | 李平   |
| 美术   | 100 | 李平   |
| 美术   |  88 | 李平   |
| 美术   |  88 | 李平   |
| 美术   |  22 | 李平   |
| 美术   |  87 | 李平   |
| 美术   |  87 | 李平   |
| 美术   |  87 | 李平 

13、查询全部学生都选修了的课程号和课程名
select
	*
from 
	student as t1,course as t2,score as t3
where 
	t3.student_id = t1.sid and t3.course_id = t2.cid
	
select distinct(t11.sid) from (select
		t1.sid
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid) as t11;
		
| sid |
+-----+
|   1 |
|   2 |
|   3 |
|   4 |
|   5 |
|   6 |
|   7 |
|   8 |
|   9 |
|  10 |
|  11 |
|  12 |
|  13 |

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '物理';
| sid | cname  |
+-----+--------+
|   1 | 物理   |
|   3 | 物理   |
|   4 | 物理   |
|   5 | 物理   |
|   6 | 物理   |
|   7 | 物理   |
|   8 | 物理   |
|   9 | 物理   |
|  10 | 物理   |
|  11 | 物理   |
|  12 | 物理  

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '生物';
| sid | cname  |
+-----+--------+
|   1 | 生物   |
|   2 | 生物   |
|   3 | 生物   |
|   4 | 生物   |
|   5 | 生物   |
|   6 | 生物   |
|   7 | 生物   |
|   8 | 生物   |
|   9 | 生物   |
|  10 | 生物   |
|  11 | 生物   |
|  12 | 生物 

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '美术';
| sid | cname  |
+-----+--------+
|   1 | 美术   |
|   2 | 美术   |
|   3 | 美术   |
|   4 | 美术   |
|   5 | 美术   |
|   6 | 美术   |
|   7 | 美术   |
|   8 | 美术   |
|   9 | 美术   |
|  10 | 美术   |
|  11 | 美术 
|  12 | 美术 	

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '体育';
		
| sid | cname  |
+-----+--------+
|   1 | 体育   |
|   2 | 体育   |
|   3 | 体育   |
|   4 | 体育   |
|   5 | 体育   |
|   6 | 体育   |
|   7 | 体育   |
|   8 | 体育   |
|   9 | 体育   |
|  10 | 体育   |
|  11 | 体育   |
|  12 | 体育   |
|  13 | 体育 

select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '美术';	
		
select
	*
from
	(select distinct(t11.sid) from (select
		t1.sid
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid) as t11) as t11 left join (select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '美术') as t22 on t11.sid = t22.sid
		left join (select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '体育') as t33 on t11.sid = t33.sid
		left join (select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '物理') as t44 on t11.sid = t44.sid
		left join (select
		t1.sid,t2.cname
	from 
		student as t1,course as t2,score as t3
	where 
		t3.student_id = t1.sid and t3.course_id = t2.cid
		and t2.cname= '生物') as t55 on t11.sid = t55.sid

| sid | sid  | cname  | sid  | cname  | sid  | cname  | sid  | cname  |
+-----+------+--------+------+--------+------+--------+------+--------+
|   1 |    1 | 美术   |    1 | 体育   |    1 | 物理   |    1 | 生物   |
|   2 |    2 | 美术   |    2 | 体育   | NULL | NULL   |    2 | 生物   |
|   3 |    3 | 美术   |    3 | 体育   |    3 | 物理   |    3 | 生物   |
|   4 |    4 | 美术   |    4 | 体育   |    4 | 物理   |    4 | 生物   |
|   5 |    5 | 美术   |    5 | 体育   |    5 | 物理   |    5 | 生物   |
|   6 |    6 | 美术   |    6 | 体育   |    6 | 物理   |    6 | 生物   |
|   7 |    7 | 美术   |    7 | 体育   |    7 | 物理   |    7 | 生物   |
|   8 |    8 | 美术   |    8 | 体育   |    8 | 物理   |    8 | 生物   |
|   9 |    9 | 美术   |    9 | 体育   |    9 | 物理   |    9 | 生物   |
|  10 |   10 | 美术   |   10 | 体育   |   10 | 物理   |   10 | 生物   |
|  11 |   11 | 美术   |   11 | 体育   |   11 | 物理   |   11 | 生物   |
|  12 |   12 | 美术   |   12 | 体育   |   12 | 物理   |   12 | 生物   |
|  13 | NULL | NULL   |   13 | 体育   | NULL | NULL   | NULL | NULL  

14、查询每门课程被选修的次数

15、查询只选修了一门课程的学生学号和姓名

16、查询所有学生考出的成绩并按从高到低排序（成绩去重）

17、查询平均成绩大于85的学生姓名和平均成绩

18、查询生物成绩不及格的学生姓名和对应生物分数

19、查询在所有选修了李平老师课程的学生中，这些课程(李平老师的课程，不是所有课程)平均成绩最高的学生姓名

20、查询每门课程成绩最好的课程id、学生姓名和分数

21、查询不同课程但成绩相同的课程号、学生号、成绩 

22、查询没学过“李平”老师课程的学生姓名以及选修的课程名称 

23、查询所有选修了学号为2的同学选修过的一门或者多门课程的同学学号和姓名 

24、任课最多的老师中学生单科成绩最高的课程id、学生姓名和分数
```














