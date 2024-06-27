#pandas.merge()  数据库风格的合并
#pandas.concat() 轴向连接，沿着一条轴，多个对象堆叠在一起
#conbine_first() 合并重叠数据


#1 pandas.merge() 方法
from pandas import DataFrame
import pandas as pd

df1=DataFrame({'name':['carl','luncy','a','b','c'],'data1':range(5)})
df2=DataFrame({'name':['carl','luncy','x','y','z'],'data2':range(5)})

#print(df1)
#print(df2)
df3=pd.merge(df1,df2,on='name',how='inner')#内连接
#print(df3)
df4=pd.merge(df1,df2,on='name',how='left') #左连接
#print(df4)
df5=df4=pd.merge(df1,df2,on='name',how='right') #右连接
#print(df5)
#按索引作为连接键
left=DataFrame({'data':range(5),'name':['Carl','Lucy','a','b','c']})
right=DataFrame({'new_data':range(5),'new_name':['chalnew','Lucynew','x','y','z']})
#print(right)
leftright=left.join(right)
#print(leftright)

#pandas.concat()方法
#轴向连接，沿着一条轴将多个对象堆叠在一起

a={"a":0,"b":1}

b={"c":2,"d":3}

c={"e":4,"f":5}



#print(pd.concat([a,c,b],axis=0)) #默认按列堆叠

#combine_first()方式
from pandas import Series

#创建序列seriesu
obj= Series([4,3,-5,9])
#print(obj)
#print(obj.index)
#print(obj.values)
obj2=Series([4,3,-5,9],index=['1/3','2/3','3/3','4/3'])

print(obj.combine_first(obj2))