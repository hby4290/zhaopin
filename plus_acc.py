#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

from matplotlib.pyplot import MultipleLocator
# 以下是字体文件路径
fontPath = "D:\zhaopin\SimHei.ttf"
# #fname指定字体文件  选简体显示中文
font = fm.FontProperties(fname=fontPath, size=10)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 这里是为了让图表正常显示中文，否则会乱码
# 以下是数据文件路径 csv格式
data = pd.read_csv('D:\zhaopin\zhaopin.csv', encoding='gbk')
print(data.shape, data.columns)
# 以下是figure（整体画面）的设置
fig = plt.figure(figsize=(10, 6), facecolor='whitesmoke')  # plt.figure 图形，在这里可以理解为画板，在画板上绘制图标。参数为设定大小
plt.grid(color='b', linestyle=':', linewidth=1, alpha=0.6)
# 将读取csv后的值赋给xy轴
x = data['name']
y = data['salary']

# 直接以xy为轴作图，label为图例
plt.plot(range(len(x)), y, 'o-', label='在籍会员数')

# 设置x轴和y轴刻度
ax = plt.gca()
#为了避免横坐标日期显示过于密集，我们设置显示日期间隔为4
#plt.xticks(range(0,len(x),4),x[0:len(x):4],size='small' ,rotation=33)

ax.yaxis.set_major_locator(MultipleLocator(10000))  # 设置y轴刻度
ax.get_yaxis().get_major_formatter().set_scientific(False)  # 去除y轴科学计数法显示
ax.spines['right'].set_visible(False)  # 去除右边框
ax.spines['top'].set_visible(False)  # 去除上边框
ax.set_facecolor('none')
plt.title('PLUS累计在籍会员数趋势')  # 折线图标题
plt.legend()
plt.show()