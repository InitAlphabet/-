# 一、导入
# 1.
# 导入matplotlib库简写为plt
import matplotlib.pyplot as plt
import numpy as np
import pandas as df

#
# 二、基本图表
2.
# 用plot方法画出x = (0, 10)
# 间sin的图像
# x = np.linspace(0, 10, 30)
# plt.plot(x, np.sin(x));
# plt.show()
# #3.
# 用点加线的方式画出x = (0, 10)
# 间sin的图像
# plt.plot(x, np.sin(x), '-o');
# plt.show()
# 4.
# 用scatter方法画出x = (0, 10)
# 间sin的点图像
# x = (0, 10)
# plt.scatter(x, np.sin(x));
# plt.show()
# 5.
# 用饼图的面积及颜色展示一组4维数据
# rng = np.random.RandomState(0)
# x = rng.randn(100)
# y = rng.randn(100)
# colors = rng.rand(100)
# sizes = 1000 * rng.rand(100)
#
# plt.scatter(x, y, c=colors, s=sizes, alpha=0.9,
#             cmap='viridis')
# plt.colorbar();  # 展示色阶
# plt.show()
# 6.
# 绘制一组误差为±0.8
# 的数据的误差条图
# x = np.linspace(0, 10, 50)
# dy = 0.8
# y = np.sin(x) + dy * np.random.randn(50)
# plt.errorbar(x, y, yerr=dy, fmt='.k')
# plt.show()

# 7.
# 绘制一个柱状图
# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [3, 1, 4, 5, 8, 9, 7, 2]
# label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
#
# plt.bar(x, y, tick_label=label);
# plt.show()
# # 8.
# 绘制一个水平方向柱状图

# plt.barh(x, y, tick_label=label);
# plt.show()
# 9.
# 绘制1000个随机值的直方图
# data = np.random.randn(1000)
# plt.hist(data);
# plt.show()
# 10.
# 设置直方图分30个bins，并设置为频率分布
# plt.hist(data, bins=30, histtype='stepfilled',density=True)
# plt.show();
# 11.
# 在一张图中绘制3组不同的直方图，并设置透明度
# x1 = np.random.normal(0, 0.8, 1000)
# x2 = np.random.normal(-2, 1, 1000)
# x3 = np.random.normal(3, 2, 1000)
#
# kwargs = dict(alpha=0.9, bins=40)
#
# plt.hist(x1, **kwargs);
# plt.hist(x2, **kwargs);
# plt.hist(x3, **kwargs);
# plt.show()
# 12.
# 绘制一张二维直方图
# mean = [0, 0]
# cov = [[1, 1], [1, 2]]
# x, y = np.random.multivariate_normal(mean, cov, 10000).T
# plt.hist2d(x, y, bins=30);
# plt.show()
# 13.
# 绘制一张设置网格大小为30的六角形直方图
# plt.hexbin(x, y, gridsize=30);
# plt.show()
# 三、自定义图表元素
# 14.
# 绘制x = (0, 10)
# 间sin的图像，设置线性为虚线
# x = np.linspace(0, 10, 100)
# plt.plot(x, np.sin(x), '--');
# 15
# 设置y轴显示范围为(-1.5, 1.5)
# x = np.linspace(0, 10, 100)
# plt.plot(x, np.sin(x))
# plt.ylim(-1.5, 1.5);
# 16.
# 设置x, y轴标签variable
# x，value
# y
# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y, label='sin(x)')
# plt.xlabel('variable x');
# plt.ylabel('value y');
# plt.show()
# 17.
# 设置图表标题“三角函数”
# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y, label='sin(x)')
# plt.title('三角函数');
# 18.
# 显示网格
# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.grid()
# plt.show()
# 19.
# 绘制平行于x轴y = 0.8
# 的水平参考线
# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.axhline(y=0.8, ls='--', c='r')
# 20.
# 绘制垂直于x轴x < 4 and x > 6
# 的参考区域，以及y轴y < 0.2 and y > -0.2
# 的参考区域
# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.axvspan(xmin=4, xmax=6, facecolor='r', alpha=0.3)  # 垂直x轴
# plt.axhspan(ymin=-0.2, ymax=0.2, facecolor='y', alpha=0.3);  # 垂直y轴
# 21.
# 添加注释文字sin(x)
# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.text(3.2, 0, 'sin(x)', weight='bold', color='r');
# plt.show()
# 22.
# 用箭头标出第一个峰值
# x = np.linspace(0.05, 10, 100)
# y = np.sin(x)
# plt.plot(x, y)
# plt.annotate('maximum', xy=(np.pi / 2, 1), xytext=(np.pi / 2 + 1, 1),
#              weight='bold',
#              color='r',
#              arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='r'));
# # 四、自定义图例
# plt.show()
# 23.
# 在一张图里绘制sin, cos的图形，并展示图例
# x = np.linspace(0, 10, 1000)
# fig, ax = plt.subplots()
#
# ax.plot(x, np.sin(x), label='sin')
# ax.plot(x, np.cos(x), '--', label='cos')
# ax.legend();
# 24.
# 调整图例在左上角展示，且不显示边框
# ax.legend(loc='upper left', frameon=False);
# fig
# 25.
# 调整图例在画面下方居中展示，且分成2列
# ax.legend(frameon=False, loc='lower center', ncol=2)
# fig
# 26.
# 绘制
# 的图像，并只显示前2者的图例
# y = np.sin(x[:, np.newaxis] + np.pi * np.arange(0, 2, 0.5))
# lines = plt.plot(x, y)
#
# # lines 是 plt.Line2D 类型的实例的列表
# plt.legend(lines[:2], ['first', 'second']);
#
# # 第二个方法
# # plt.plot(x, y[:, 0], label='first')
# # plt.plot(x, y[:, 1], label='second')
# # plt.plot(x, y[:, 2:])
# # plt.legend(framealpha=1, frameon=True);
# 27.
# 将图例分不同的区域展示
# fig, ax = plt.subplots()
#
# lines = []
# styles = ['-', '--', '-.', ':']
# x = np.linspace(0, 10, 1000)
#
# for i in range(4):
#     lines += ax.plot(x, np.sin(x - i * np.pi / 2), styles[i], color='black')
# ax.axis('equal')
#
# # 设置第一组标签
# ax.legend(lines[:2], ['line A', 'line B'],
#           loc='upper right', frameon=False)
#
# # 创建第二组标签
# from matplotlib.legend import Legend
#
# leg = Legend(ax, lines[2:], ['line C', 'line D'],
#              loc='lower right', frameon=False)
# ax.add_artist(leg);
# 五、自定义色阶
# 28.
# 展示色阶
# x = np.linspace(0, 10, 1000)
# I = np.sin(x) * np.cos(x[:, np.newaxis])
#
# plt.imshow(I)
# plt.colorbar();
# plt.show()
# 29.
# 改变配色为
# 'gray'
# plt.imshow(I, cmap='gray');
# 30.
# 将色阶分成6个离散值显示
# plt.imshow(I, cmap=plt.cm.get_cmap('Blues', 6))
# plt.colorbar()
# plt.clim(-1, 1);
# 六、多子图
# 31.
# 在一个1010的画布中，(0.65, 0.65)
# 的位置创建一个0
# .20
# .2
# 的子图
# ax1 = plt.axes()
# ax2 = plt.axes([0.65, 0.65, 0.2, 0.2])
# 32.
# 在2个子图中，显示sin(x)
# 和cos(x)
# 的图像
# fig = plt.figure()
# ax1 = fig.add_axes([0.1, 0.5, 0.8, 0.4], ylim=(-1.2, 1.2))
# ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.4], ylim=(-1.2, 1.2))
#
# x = np.linspace(0, 10)
# ax1.plot(np.sin(x));
# ax2.plot(np.cos(x));
# plt.show()
# 33.
# 用for创建6个子图，并且在图中标识出对应的子图坐标
# for i in range(1, 7):
#     plt.subplot(2, 3, i)
#     plt.text(0.5, 0.5, str((2, 3, i)), fontsize=18, ha='center')
#     plt.show()

# # 方法二
# fig = plt.figure()
# fig.subplots_adjust(hspace=0.4, wspace=0.4)
# for i in range(1, 7):
#     ax = fig.add_subplot(2, 3, i)
#     ax.text(0.5, 0.5, str((2, 3, i)),fontsize=18, ha='center')
#     plt.show()
# 34.
# 设置相同行和列共享x, y轴
# fig, ax = plt.subplots(2, 3, sharex='col', sharey='row')
# 35.
# 用[]
# 的方式取出每个子图，并添加子图座标文字
# for i in range(2):
#     for j in range(3):
#         ax[i, j].text(0.5, 0.5, str((i, j)), fontsize=18, ha='center')
# fig
# 36.
# 组合绘制大小不同的子图，样式如下
#
# grid = plt.GridSpec(2, 3, wspace=0.4, hspace=0.3)
# plt.subplot(grid[0, 0])
# plt.subplot(grid[0, 1:])
# plt.subplot(grid[1, :2])
# plt.subplot(grid[1, 2]);
# plt.show()
# 37.
# 显示一组二维数据的频度分布，并分别在x, y轴上，显示该维度的数据的频度分布
# mean = [0, 0]
# cov = [[1, 1], [1, 2]]
# x, y = np.random.multivariate_normal(mean, cov, 3000).T
#
# # Set up the axes with gridspec
# fig = plt.figure(figsize=(6, 6))
# grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)
# main_ax = fig.add_subplot(grid[:-1, 1:])
# y_hist = fig.add_subplot(grid[:-1, 0], xticklabels=[], sharey=main_ax)
# x_hist = fig.add_subplot(grid[-1, 1:], yticklabels=[], sharex=main_ax)
#
# # scatter points on the main axes
# main_ax.scatter(x, y, s=3, alpha=0.2)
#
# # histogram on the attached axes
# x_hist.hist(x, 40, histtype='stepfilled',
#             orientation='vertical')
# x_hist.invert_yaxis()
#
# y_hist.hist(y, 40, histtype='stepfilled',
#             orientation='horizontal')
# y_hist.invert_xaxis()
# 七、三维图像
# 38.
# 创建一个三维画布
from mpl_toolkits import mplot3d

# fig = plt.figure()
# # ax = plt.axes(projection='3d')
# # plt.show()
# 39.
# 绘制一个三维螺旋线
# ax = plt.axes(projection='3d')
# #
# # # Data for a three-dimensional line
# zline = np.linspace(0, 15, 1000)
# xline = np.sin(zline)
# yline = np.cos(zline)
# ax.plot3D(xline, yline, zline);
# plt.show()

# 40.
# 绘制一组三维点
ax = plt.axes(projection='3d')
zdata = 15 * np.random.random(100)
xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
# 八、宝可梦数据集可视化
# 41.
# 展示前5个宝可梦的Defense, Attack, HP的堆积条形图
# pokemon = df['Name'][:5]
# hp = df['HP'][:5]
# attack = df['Attack'][:5]
# defense = df['Defense'][:5]
# ind = [x for x, _ in enumerate(pokemon)]
#
# plt.figure(figsize=(10, 10))
# plt.bar(ind, defense, width=0.8, label='Defense', color='blue', bottom=attack + hp)
# plt.bar(ind, attack, width=0.8, label='Attack', color='gold', bottom=hp)
# plt.bar(ind, hp, width=0.8, label='Hp', color='red')
#
# plt.xticks(ind, pokemon)
# plt.ylabel("Value")
# plt.xlabel("Pokemon")
# plt.legend(loc="upper right")
# plt.title("5 Pokemon Defense & Attack & Hp")
#
# plt.show()
# 42.
# 展示前5个宝可梦的Attack, HP的簇状条形图
# N = 5
# pokemon_hp = df['HP'][:5]
# pokemon_attack = df['Attack'][:5]
#
# ind = np.arange(N)
# width = 0.35
# plt.bar(ind, pokemon_hp, width, label='HP')
# plt.bar(ind + width, pokemon_attack, width, label='Attack')
#
# plt.ylabel('Values')
# plt.title('Pokemon Hp & Attack')
#
# plt.xticks(ind + width / 2, (df['Name'][:5]), rotation=45)
# plt.legend(loc='best')
# plt.show()
# 43.
# 展示前5个宝可梦的Defense, Attack, HP的堆积图
# x = df['Name'][:4]
# y1 = df['HP'][:4]
# y2 = df['Attack'][:4]
# y3 = df['Defense'][:4]
#
# labels = ["HP ", "Attack", "Defense"]
#
# fig, ax = plt.subplots()
# ax.stackplot(x, y1, y2, y3)
# ax.legend(loc='upper left', labels=labels)
# plt.xticks(rotation=90)
# plt.show()
# 44.
# 公用x轴，展示前5个宝可梦的Defense, Attack, HP的折线图
# x = df['Name'][:5]
# y1 = df['HP'][:5]
# y2 = df['Attack'][:5]
# y3 = df['Defense'][:5]
#
# # Create two subplots sharing y axis
# fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=True)
#
# ax1.plot(x, y1, 'ko-')
# ax1.set(title='3 subplots', ylabel='HP')
#
# ax2.plot(x, y2, 'r.-')
# ax2.set(xlabel='Pokemon', ylabel='Attack')
#
# ax3.plot(x, y3, ':')
# ax3.set(xlabel='Pokemon', ylabel='Defense')
#
# plt.show()
# 45.
# 展示前15个宝可梦的Attack, HP的折线图
# plt.plot(df['HP'][:15], '-r', label='HP')
# plt.plot(df['Attack'][:15], ':g', label='Attack')
# plt.legend();
# 46.
# 用scatter的x, y, c属性，展示所有宝可梦的Defense, Attack, HP数据
# x = df['Attack']
# y = df['Defense']
# colors = df['HP']
#
# plt.scatter(x, y, c=colors, alpha=0.5)
# plt.title('Scatter plot')
# plt.xlabel('HP')
# plt.ylabel('Attack')
# plt.colorbar();
# 47.
# 展示所有宝可梦的攻击力的分布直方图，bins = 10
# x = df['Attack']
# num_bins = 10
# n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5)
# plt.title('Histogram')
# plt.xlabel('Attack')
# plt.ylabel('Value')
# plt.show()
# 48.
# 展示所有宝可梦Type
# 1
# 的饼图
# plt.figure(1, figsize=(8, 8))
# df['Type 1'].value_counts().plot.pie(autopct="%1.1f%%")
# plt.legend()
# 49.
# 展示所有宝可梦Type
# 1
# 的柱状图
# ax = df['Type 1'].value_counts().plot.bar(figsize=(12, 6), fontsize=14)
# ax.set_title("Pokemon Type 1 Count", fontsize=20)
# ax.set_xlabel("Pokemon Type 1", fontsize=20)
# ax.set_ylabel("Value", fontsize=20)
#
# plt.show()
# 50.
# 展示综合评分最高的10只宝可梦的系数间的相关系数矩阵
# import seaborn as sns
#
# top_10_pokemon = df.sort_values(by='Total', ascending=False).head(10)
# corr = top_10_pokemon.corr()
#
# fig, ax = plt.subplots(figsize=(10, 6))
# sns.heatmap(corr, annot=True)
# ax.set_ylim(9, 0)
# plt.show()
# #
