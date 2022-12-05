import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontPath = "D:\zhaopin\simhei.ttf"
font = fm.FontProperties(fname=fontPath, size=10)

data = pd.read_csv('D:\zhaopin\ZHAOPIN.xls', encoding="'ISO-8859-1")
print(data.shape, data.columns)

fig = plt.figure(figsize=(6, 5), facecolor='whitesmoke')

# 标签内容
labels = data['jobPlace'].value_counts().index
# 偏移扇区
explodes = [0.05 if i == "北京" else 0 for i in labels]
# 设置颜色 颜色最好还是自己写 饼图会根据所给出的颜色进行循环使用。
colors = ['#7AC5CD', '#76EE00', '#71C671', '#68838B', '#757575']

patchs, l_text, p_text = plt.pie(data['城市'].value_counts(), labels=labels, autopct="%1.1f%%", colors=colors,
                                 explode=explodes, shadow=False, labeldistance=1.1, startangle=90)

# 设置透明度 因为饼图中并没有alpha参数，所以要用这种方法来设置
for i, p in enumerate(patchs):
    p.set_alpha(0.4)
# 设定字体
plt.title('招聘城市分布情况', fontproperties=font)
for t in (l_text + p_text):
    t.set_fontproperties(font)
plt.show()  # 显示图表