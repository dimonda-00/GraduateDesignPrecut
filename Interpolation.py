#外部引用
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
#内部引用
from InnerTools import Class3DData


#数据源
My3DData = Class3DData()
print(type(My3DData.Y))
print(My3DData.NumberOfData)
points = np.random.rand(195, 2)  # n是已知点个数
values = My3DData.Z  # 对应没每个点的值
# 插值的目标

# 注意，这里和普通使用数组的维度、下标不一样，是因为如果可视化的话，imshow坐标轴和一般的不一样
end1 = max(My3DData.X)
start1 = min(My3DData.X)
start2 = min(My3DData.Y)
end2 = max(My3DData.Y)
step1 = 0.1
step2 = step1
x, y = np.mgrid[
        end1:start1:step1 * 1j,
        start2:end2:step2 * 1j]

# grid就是插值结果，你想要的到的区间的每个点数据都在这个grid矩阵里
grid = griddata(points, values, (x, y), method="cubic", fill_value=0)

# 这里通过imshow显示时，坐标思维要按照计算机的来，普通图片是2维数组
# x 是最终结果的第一维，下标是从上到下由零增加
# y 是最终结果的第二维，下标是从左到右由零增加



plt.subplot(1, 1, 1)
plt.title("0°")
plt.imshow(grid, cmap='jet')  # contourf jet gray
plt.colorbar()
plt.show()