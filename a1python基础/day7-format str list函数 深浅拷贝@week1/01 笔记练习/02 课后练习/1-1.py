# ### 字符串的格式化format
# (1)顺序传参
# {}是format中的占位符
strvar = '{}向{}开了一枪,饮弹而亡'.format('赵沈阳','需保障')
print(strvar)  #赵沈阳向需保障开了一枪,饮弹而亡

# (2)索引传参
strvar = '{1}向{0}开了一枪,饮弹而亡'.format('赵沈阳','需保障')
print(strvar)  #需保障向赵沈阳开了一枪,饮弹而亡

# (3)关键字传参
strvar = '{who1}摸了{who2}一下,回头一巴掌'.format(who1='王伟',who2='马春妮')
strvar = '{who1}摸了{who2}一下,回头一巴掌'.format(who1='马春妮',who2='王伟')
print(strvar)  #马春妮摸了王伟一下,回头一巴掌

# (4)容器类型数据(列表或元组)传参
# 方法一
strvar = '{0[0]}摸了{1[1]}一下,嘿嘿一笑,有戏'.format(['赵峰拥','赵世超'],['王雨涵','王同佩'])
print(strvar)  #赵峰拥摸了王同佩一下,嘿嘿一笑,有戏

# 方法二(推荐)
strvar = '{group1[0]}摸了{group2[1]}一下,嘿嘿一笑,有戏'\
.format(group1=['赵峰拥','赵世超'],group2=['王雨涵','王同佩'])
print(strvar)  #赵峰拥摸了王同佩一下,嘿嘿一笑,有戏

# 方法三(推荐)
# 注意一:如果改容器是字典,通过键取值时,不需要加引号
# 注意二:通过下标取值时,不能使用负号(逆向索引)
# strvar = '{group1[zfy]摸了{group2[1]}一下,嘿嘿一笑,有戏}'.format(group1={'zfy':'赵峰拥','zsc':'赵世超'},group2=('王雨涵','王同佩'))
#
# strvar = "{group1[zfy]}摸了{group2[-1]}一下,嘿嘿一笑,有戏".format(group1={"zfy":"赵蜂拥","zsc":"赵世超"} , group2 = ("王雨涵","王同培"))
# strvar = "{group1[zfy]}摸了{group2[1]}一下,嘿嘿一笑,有戏".format(group1={'zfy':'赵峰拥','zsc':'赵世超'},  group2=("王雨涵","王同培"))
strvar = "{group1[zfy]}摸了{group2[1]}一下,嘿嘿一笑,有戏".format(group1={'zfy':'赵峰拥','zsc':'赵世超'},group2=('王雨涵','王同佩'))
# 注意:摸了前面少了一个}



















