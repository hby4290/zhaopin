#coding=utf-8
import pandas as pd
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator

# 以下是字体文件路径
fontPath = "D:\zhaopin\simhei.ttf"
# fname指定字体文件  选简体显示中文
font = fm.FontProperties(fname=fontPath, size=10)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 以下是数据文件路径 csv格式
data = pd.read_csv('D:\zhaopin\zhaopin.csv', encoding='gbk')
print(data.shape, data.columns)

# 以下是figure（整体画面）的设置
fig = plt.figure(figsize=(8, 6), facecolor='whitesmoke')

# 新老用户比例
# 标签内容
labels = data['jobPlace'].value_counts().index
# 偏移扇区
explodes = [0.05 if i == 1 else 0 for i in labels]
# 设置颜色 颜色最好还是自己写 饼图会根据所给出的颜色进行循环使用。
colors = "m", "blue"

patchs, l_text, p_text = plt.pie(data['jobPlace'].value_counts(), labels=["北京", "上海"], autopct="%1.1f%%", colors=colors,
                                 explode=explodes, shadow=False, labeldistance=1.1, startangle=90)

# 设置透明度 因为饼图中并没有alpha参数，所以要用这种方法来设置
for i, p in enumerate(patchs):
    p.set_alpha(0.4)
# 设定字
plt.title('新老用户比例', fontproperties=font)
for t in (l_text + p_text):
    t.set_fontproperties(font)

plt.show()  # 显示图表