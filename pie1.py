import pymysql
import matplotlib.pyplot as plt
import numpy as np
# 1.打开数据库连接
con_engine = pymysql.connect(host = '192.168.3.186' ,user = 'root',password='123456',database = 'edu7out', port=3306, charset = 'utf8')
# 2.使用 cursor() 方法创建一个游标对象 cursor

cursor = con_engine.cursor()
sql_ = "select * from ismobilesql;"
# 使用 execute()  方法执行 SQL 查询
cursor.execute(sql_)
# 使用 fetchall() 方法获取多条数据
results = cursor.fetchall()
print(results)
#将二维数组转换为一维数组，再将一维数组中的num输出，并查看结果
a = list(np.array(results).flatten())
slices = list(np.array(a[1::2]))
print(slices)
cursor.close()


#绘制面板
plt.figure(figsize=(6,6))
#显示中文及负号
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
activities = ['PC端','移动端']
plt.title('移动端和PC端比例')
colors = ['#2F4554','#C23531']
plt.pie(slices,labels=activities,shadow=False,colors=colors,labeldistance=1.1,counterclock=False,startangle=90,pctdistance=0.9)
plt.legend(loc='upper left', bbox_to_anchor=(-0.1,1))
plt.show()