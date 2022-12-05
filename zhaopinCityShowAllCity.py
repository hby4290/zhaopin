import pymysql
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import MultipleLocator

#绘制面板
fig = plt.figure(figsize=(12,8))
#ax = fig.gca()
#显示中文及负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

# 1.打开数据库连接
con_engine = pymysql.connect(host = '192.168.3.186' ,user = 'root',password='123456',database = 'db_zhaopin', port=3306, charset = 'utf8')

# 2.使用 cursor() 方法创建一个游标对象 cursor
cursor = con_engine.cursor()

#----------------------------------beijing
sql_ = "select * from beijing;"
cursor.execute(sql_)
results = cursor.fetchall()
a = list(np.array(results).flatten())
slices = list(np.array(a[1::2]))
activities = list(np.array(a[::2]))

ax1=plt.subplot(2,2,1)
plt.sca(ax1)
plt.title('北京市大数据岗位招募情况')
colors = ['#88585C','#636B6E','#61A0A9']
explode = (0,0.1,0.2)
pie =  plt.pie(slices,labels=activities,explode=explode,shadow=False,colors=colors,labeldistance=1.1,counterclock=False,startangle=90)
plt.axis('equal')


#----------------------------------shanghai
sql_ = "select * from shanghai;"
cursor.execute(sql_)
results = cursor.fetchall()
a = list(np.array(results).flatten())
slices = list(np.array(a[1::2]))
activities = list(np.array(a[::2]))

ax2=plt.subplot(2,2,2)
plt.sca(ax2)
plt.title('上海市大数据岗位招募情况')
colors = ['#88585C','#636B6E','#61A0A9']
explode = (0,0.1,0.2)
pie =  plt.pie(slices,labels=activities,explode=explode,shadow=False,colors=colors,labeldistance=1.1,counterclock=False,startangle=90)
plt.axis('equal')


#----------------------------------chengdu
sql_ = "select * from chengdu;"
cursor.execute(sql_)
results = cursor.fetchall()
a = list(np.array(results).flatten())
slices = list(np.array(a[1::2]))
activities = list(np.array(a[::2]))

ax3=plt.subplot(2,2,3)
plt.sca(ax3)
plt.title('成都市大数据岗位招募情况')
colors = ['#88585C','#636B6E','#61A0A9']
explode = (0,0.1,0.2)
pie =  plt.pie(slices,labels=activities,explode=explode,shadow=False,colors=colors,labeldistance=1.1,counterclock=False,startangle=90)
plt.axis('equal')


#----------------------------------chongqing
sql_ = "select * from chongqing;"
cursor.execute(sql_)
results = cursor.fetchall()
a = list(np.array(results).flatten())
slices = list(np.array(a[1::2]))
activities = list(np.array(a[::2]))

ax4=plt.subplot(2,2,4)
plt.sca(ax4)
plt.title('重庆市大数据岗位招募情况')
colors = ['#88585C','#636B6E','#61A0A9']
explode = (0,0.1,0.2)
pie =  plt.pie(slices,labels=activities,explode=explode,shadow=False,colors=colors,labeldistance=1.1,counterclock=False,startangle=90)
plt.axis('equal')

plt.gcf().autofmt_xdate()

plt.show()