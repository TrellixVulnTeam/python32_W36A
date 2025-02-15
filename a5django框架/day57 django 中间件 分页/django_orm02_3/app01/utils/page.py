#!/usr/bin/env python
#-*- coding:utf-8 -*-
#@author: wangtongpei
#@time:  2020/12/4 20:29

from django.utils.safestring import mark_safe
# 标识字符串是安全的,可以直接展示成标签,前端页面不需要用safe过滤器

# class Pagenation():
class Pagenation:
	def __init__(self,current_page,total_count):
	# 参数1是当前是第几页
	# 参数2是总记录数
		self.per_page_num = 3  ## 每页展示3条数据
		self.current_page = current_page

		total_page_number,b = divmod(total_count,self.per_page_num)
	# 总页码数量
		if b: #如果有余数,就+1
			total_page_number += 1

		show_page_number = 11 # 总共展示11个页码

		half_page_number = show_page_number // 2
		if current_page <= half_page_number:
			# 前5页的分页展示完全一样,写死,显示1-11页
			page_number_start = 1
			page_number_end = show_page_number + 1
			# range左闭右开
		elif (current_page + half_page_number) > total_page_number:
			# 最后5页的分页展示完全一样,写死,显示最后5页
			page_number_start = total_page_number - show_page_number + 1
			page_number_end = total_page_number + 1
			# range左闭右开
		else:
			page_number_start = current_page - half_page_number  #6
			page_number_end = current_page + half_page_number + 1 #16

		self.page_num_range = range(page_number_start,page_number_end)

	@property  #方法转属性
	def page_data_start(self):
		return (self.current_page - 1) * self.per_page_num

	@property
	def end_data_start(self):
		return self.current_page * self.per_page_num

	def page_html(self):
		# 把字符串拼接好,发送给前端作为标签展示
		page_html_start = '''
			<nav aria-label="Page navigation">
			  <ul class="pagination">
			    <li>
			      <a href="#" aria-label="Previous">
			        <span aria-hidden="true">&laquo;</span>
			      </a>
			    </li>
		'''

		for i in self.page_num_range:
			s = f'<li><a href="?page={i}">{i}</a></li>'
			page_html_start += s

		page_html_end = '''
		    <li>
		      <a href="#" aria-label="Next">
		        <span aria-hidden="true">&raquo;</span>
		      </a>
		    </li>
		  </ul>
		</nav>
		'''
		page_all_html = page_html_start + page_html_end
		return mark_safe(page_all_html)
# 标识字符串是安全的,可以直接展示成标签,前端页面不需要用safe过滤器

'''
<nav aria-label="Page navigation">
  <ul class="pagination">
    <li>
      <a href="#" aria-label="Previous">
        <span aria-hidden="true">&laquo;</span>
      </a>
    </li>
    <li><a href="#">1</a></li>
    <li><a href="#">2</a></li>
    <li><a href="#">3</a></li>
    <li><a href="#">4</a></li>
    <li><a href="#">5</a></li>
    <li>
      <a href="#" aria-label="Next">
        <span aria-hidden="true">&raquo;</span>
      </a>
    </li>
  </ul>
</nav>
'''














