#外部引用
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import pandas as pd
#内部引用

#数据导入和三维切片
class Class3DData:
    def __init__(self):
        # 数据来源
        location = r'C:\Users\胡剑宁\Files\CodeBox\Precut\Dataset\FinalDataset.csv'
        MainDf = pd.read_csv(location)
        ValueOfPosition = MainDf.values
        # 位置数据
        self.X = ValueOfPosition[:,1]
        self.Y = ValueOfPosition[:,2]
        self.Z = ValueOfPosition[:,3]
        # 数据属性
        self.NumberOfData  = len(self.X)


        