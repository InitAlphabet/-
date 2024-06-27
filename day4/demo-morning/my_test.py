from matplotlib import pyplot as plt
import numpy as np

# 字体防止中文不显示
plt.rcParams['font.sans-serif'] = ['SimHei']
# -号显示问题
plt.rcParams['axes.unicode_minus'] = False
# # 生成等间距x列表
# x = np.linspace(start=0, num=20, stop=10)
# # 画布
# figure1 = plt.figure(figsize=(8, 6))  # 宽高
# # 画布切割为2*2，生成图一的位置1，左上角
# ax1 = figure1.add_subplot(2, 2, 1)  # 设置图片位置
# ax1.set_title("plot")
# ax1.plot(x, np.sin(x), linestyle='-', marker='o', color='#323232')
# # 画布切割为2*2，生成图2的位置2，右上角
# ax2 = figure1.add_subplot(2, 2, 2)
# ax2.scatter(x, np.sin(x))
# ax2.set_title("scatter")
#
# # 4 维散点图
# ax3 = figure1.add_subplot(2, 2, 3)
# ax3.set_title("4-dim")
# random_generator = np.random.RandomState(2)  # 伪随机生成器，设置种子2
# x = random_generator.randn(100)  # 生成100个[0,1),正态分布的数
# y = random_generator.randn(100)
# colors = random_generator.rand(100)  # 均匀分布
# sizes = 1000 * random_generator.rand(100)
# sc = ax3.scatter(x, y, s=sizes, alpha=0.9, c=colors, cmap='viridis')
# plt.colorbar(sc, ax=ax3)  # 展示色阶
#
# # 散点图
# ax4 = figure1.add_subplot(2, 2, 4)
# ax4.set_title("error_bar")
# x = np.linspace(0, 10, 40)
# dy = 0.8
# y = np.sin(x) + dy * np.random.randn(40)
# ax4.errorbar(x, y, yerr=dy, fmt=".r")
# # 全部绘制
# plt.show()


# figure2 = plt.figure(figsize=(10, 8))
# ax21 = figure2.add_subplot(2, 2, 1)
# ax21.set_title("柱状图")
# x = np.arange(0, 9, 1)
# y = np.random.randint(1, 10, 9)
# func = lambda x: chr(ord('A') + x)
# label = [func(i) for i in range(9)]
# ax21.bar(x, y, tick_label=label)
#
# ax22 = figure2.add_subplot(2, 2, 2)
# ax22.set_title("水平柱状图")
# ax22.barh(x, y, tick_label=label)
#
# ax23 = figure2.add_subplot(2, 2, 3)
# ax23.set_title("随机直方频率图")
# data = np.random.randn(1000)
# ax23.hist(data, bins=30, histtype='stepfilled',density=True,alpha=0.7)
#
# ax24 = figure2.add_subplot(2, 2, 4)
# ax24.set_title("绘制一张二维直方图")
# mean = [0, 0]
# cov = [[1, 1], [1, 2]]
# x, y = np.random.multivariate_normal(mean, cov, 10000).T
# ax24.hist2d(x, y, bins=30)
# plt.show()

# plt.hexbin(x, y, gridsize=30)
# plt.show()


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')


# 参数化球体的函数
def sphere(u, v):
    x = np.sin(u) * np.cos(v)
    y = np.sin(u) * np.sin(v)
    z = np.cos(u)
    return x, y, z


# 创建参数范围
u = np.linspace(0, np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
U, V = np.meshgrid(u, v)
print(U,V)
# 计算球体的坐标
X, Y, Z = sphere(U, V)

# 绘制球体
ax.plot_surface(X, Y, Z, color='b', alpha=0.6)

# 设置图形标题
ax.set_title('Sphere')

# # 显示图形
# plt.show()
