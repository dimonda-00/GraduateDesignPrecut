#引用库
import pandas as pd
import numba #for循环加速，可不用
import re

'''从cad中提取出的数据集'''
df = pd.read_csv("C:/Users/胡剑宁/Files/CodeBox/Precut/Dataset/TestForPy1.csv")
#print(type(df))

''''选择所有圆对象的位置'''
def CirclePlace():
    CircleDf = df[df['名称'] == '圆'] 
    CircleDf =  CircleDf[CircleDf['直径'].isin([7.3677])] #选择钻井在煤层的实际位置
    #CircleDf =  CircleDf[CircleDf['直径'].isin([10.0349])] 
    CircleDf =  CircleDf[['直径','中心 X','中心 Y']] 
    CircleDf =  CircleDf[['中心 X','中心 Y']] 
    #CircleDf.to_csv(r'C:\Users\胡剑宁\Files\CodeBox\Precut\Dataset\CircPlace.csv',sep=',',index=True,header=True)
    return CircleDf
 
'''选择所有钻井深度数据和位置数据'''
def Depth():
    DepthDf = df[df['名称'] == '多行文字']
    DepthDf = DepthDf[['内容','位置 X','位置 Y']]
    Bool = DepthDf.内容.str.contains('C7')#依据颜色筛选内容内的深度值
    DepthDf = DepthDf[Bool]
    MidDf = DepthDf['内容'].str.split(";",expand=True)
    MidDf = MidDf[2].str.split("}",expand=True)
    DepthDf['深度0']=MidDf[0]
    DepthDf = DepthDf[DepthDf.深度0.str.contains('[-+]?\d+(?:,\d+)?(?:\.\d+)?')]#选择数字
    DepthDf = DepthDf[~DepthDf.深度0.str.contains('∠|焦|深|工|E')]#去除角度和汉字
    DepthDf = DepthDf[~(DepthDf['深度0'].astype(float)%1 == 0) ]#去除整数（深度等高线残留）
    DepthDf = DepthDf[(DepthDf['深度0'].astype(float)<= 0) ]#去除正数（地面标高）
    DepthDf = DepthDf[['位置 X','位置 Y','深度0'] ]
    #DepthDf.to_csv(r'C:\Users\胡剑宁\Files\CodeBox\Precut\Dataset\depth.csv',sep=',',index=True,header=True)
    return DepthDf

'''为每个钻井位置匹配深度'''
def MatchDeep(CirclePlace,Depth):
    print()
    MatchMap = pd.DataFrame(columns=['PositionX','PositionY','depth'])
    for index,row in CirclePlace.iterrows():
        PositionX = row['中心 X']
        PositionY = row['中心 Y']
        MatchDict = {}
        for index,row in Depth.iterrows():#遍历第二个dataframe并取得距离最小
            PositionXX = row['位置 X']
            PositionYY = row['位置 Y']
            Distance = (PositionX-PositionXX)*(PositionX-PositionXX) +(PositionY-PositionYY)*(PositionY-PositionYY)
            depth = row['深度0']
            tempDict = {depth:Distance}
            MatchDict.update(tempDict)
        #print(MatchDict)
        WantDepth = min(MatchDict,key=MatchDict.get)
        tempData = {'PositionX':PositionX,'PositionY':PositionY,'depth':WantDepth}
        tempDf = pd.DataFrame(data=tempData,index=[0])
        MatchMap =  pd.concat([MatchMap, tempDf],ignore_index=True)
        print('---Working---')
        #print(tempDf)
        #print(WantDepth)
    MatchMap = MatchMap[['PositionX','PositionY','depth']]# 没啥用
    #MatchMap.to_csv(r'C:\Users\胡剑宁\Files\CodeBox\Precut\Dataset\FinalDataset.csv',sep=',',index=True,header=True)
    MatchMap.to_csv(r'C:\Users\胡剑宁\Files\CodeBox\Precut\Dataset\FinalDataset.txt',sep=',',index=False,header=False)
    #print(MatchMap) 
    return MatchMap 
     
              
    

if __name__ == "__main__":
    print ('This is main of module "DataExtract.py"')
    #print(CirclePlace())
    #print(Depth())
    MatchDeep(CirclePlace(),Depth())
    


