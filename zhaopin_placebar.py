import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

# 以下是字体文件路径
fontPath = "D:\zhaopin\simhei.ttf"
# #fname指定字体文件  选简体显示中文
font = fm.FontProperties(fname=fontPath, size=10)

data = pd.read_csv('D:\zhaopin\zhaopin.csv', encoding="gbk")
print(data.shape, data.columns)

# 以下是figure（整体画面）的设置
fig = plt.figure(figsize=(6, 5), facecolor='whitesmoke')

# 先划分四个年龄区间
bins = ['北京', '上海', '天津', '成都']

cut = pd.cut(data['jobPlace'], bins=bins)
print(cut)
#统计每个年龄区间个数
cuts = pd.value_counts(cut)
print(cuts)


jobPlace = dict(zip(cuts.index.values.tolist(), cuts.tolist()))
# print(age)
jobPlace0 = sorted(jobPlace)
# print(age[age0[0]])
jobPlacenum = []
for i in range(len(jobPlace0)):
    jobPlacenum.append(jobPlace[jobPlace0[i]])
    print(jobPlace0, jobPlacenum)

plt.bar(range(len(jobPlacenum)), list(jobPlacenum), align='center', color='darkorange', alpha=0.6, width=0.4)

# 显示数据标签
for a,b in zip(range(len(jobPlacenum)), list(jobPlacenum)):
    plt.text(a,b,
             b,
             ha='center',
             va='bottom',
             )
plt.title('招聘城市分布情况')

labels = ['北京', '上海', '天津', '成都']
plt.xticks(range(len(jobPlace0)), labels, rotation=0)
# XY轴信息
plt.xlabel('招聘城市')
plt.ylabel('数目')
# 下面是一种写法，当前的图表和子图可以使用plt.gcf()和plt.gca()获得，分别表示Get Current Figure和Get Current Axes
d = plt.gca()
d.yaxis.get_label().set_fontproperties(font)  # 设定字体
d.xaxis.get_label().set_fontproperties(font)  # 设定字体
d.set_facecolor("none")  # 设置背景色 这里是透明
# 隐藏右边界和上边界，为了美观
d.spines["right"].set_color("none")
d.spines["top"].set_color("none")


# 标题、横纵坐标字体设置，这种统一设置的写法很常用
for label in ([d.title] + d.get_xticklabels() + d.get_yticklabels()):
    label.set_fontproperties(font)

plt.show()