import pymysql
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
con_engine = pymysql.connect(host = '192.168.3.186' ,user = 'root',password='123456',database = 'db_zhaopin', port=3306, charset = 'utf8')
cursor = con_engine.cursor()
sql_ = "select * from chengdu;"
cursor.execute(sql_)
results = cursor.fetchall()
print(results)
a = list(np.array(results).flatten())
slices = list(np.array(a[1::2]))
print(slices)
activities = list(np.array(a[::2]))
print(activities)
cursor.close()


#显示中文及负号
plt.title('成都市大数据岗位招募情况')

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

colors = ['#88585C','#636B6E','#61A0A9']
explode = (0,0.1,0.2)
pie =  plt.pie(slices,labels=activities,explode=explode,shadow=False,colors=colors,labeldistance=1.1,counterclock=False,startangle=90)

plt.axis('equal')
plt.show()