#外部引用
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy 
import pandas as pd
#数据源
location = r'C:\Users\胡剑宁\Files\CodeBox\Precut\Dataset\FinalDataset.csv'
MainDf = pd.read_csv(location)
print('imported!')



def Darwplot(x,y,z):
    #定义坐标轴
    fig = plt.figure()
    ax1 = plt.axes(projection='3d')
    #ax = fig.add_subplot(111,projection='3d')  #这种方法也可以画多个子图
    
    ax1.scatter3D(x,y,z, cmap='Blues')  #绘制散点图
    ax1.plot_trisurf(x,y,z,cmap='rainbow')#绘制三角面
    ax1.set_aspect('equal')
    #ax1.contour(x,y,z, zdim='z',offset=-2,cmap='rainbow') 
    #等高线图，要设置offset，为Z的最小值
    plt.show()


if __name__ == "__main__":
    print ('This is main of module "MapNaking.py"')
    ValueOfPosition = MainDf.values
    X = ValueOfPosition[:,1]
    Y = ValueOfPosition[:,2]
    Z = ValueOfPosition[:,3]
    Darwplot(X,Y,Z)
    
    