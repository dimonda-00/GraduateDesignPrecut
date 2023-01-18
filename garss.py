#外部引用
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
#内部引用
from InnerTools import Class3DData


#数据源
My3DData = Class3DData()
X1 = My3DData.X.reshape(-1,1)
Y1 = My3DData.Y.reshape(-1,1)
Z1 = My3DData.Z.reshape(-1,1)
points = np.hstack((X1,Y1))  
values = My3DData.Z  # 对应每个点的值
print(points)
