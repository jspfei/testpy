# -*- coding: utf-8 -*-
import json

path = 'E:\mywork\pythonwork\pydata-book-master\ch02\usagov_bitly_data2012-03-16-1331923249.txt'
#read all data by path
print open(path).readline()

#json to dict
records = [json.loads(line) for line in open(path)]



from pandas import DataFrame,Series

import pandas as pd ; import numpy as np


frame = DataFrame(records)

print frame

print frame['tz'][:10]

tz_counts = frame['tz'].value_counts()
print tz_counts[:10]

# 利用绘图库 matplotlib为这段数据生成一张图片
# 为缺失数据添加替代值
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] ='Unknown'

tz_counts = clean_tz.value_counts()
print tz_counts[:10]

# 显示数据
import matplotlib.pyplot as plt
#plt.plot(tz_counts[:10],tz_counts[:10], 'k--')
# plt.show() 



results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]

cframe = frame[frame.a.notnull()]

operatin_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')

print operatin_system[:5]

#时区，操作系统列表分组

by_tz_os = cframe.groupby(['tz',operatin_system])

agg_counts = by_tz_os.size().unstack().fillna(0)

print agg_counts[:10]
#39页
indexer = agg_counts.sum(1).argsort()
print agg_counts.sum(1).argsort()
print indexer[:10]

count_subset = agg_counts.take(indexer)[-10:]

print count_subset

#pylab 第一次调用成功， 用pl.show()
import matplotlib.pylab as pl
import numpy as np
count_subset.plot(kind='barh',stacked=True)
#pl.show()

#三维绘图
# from pylab import *
# from mpl_toolkits.mplot3d import Axes3D
# 
# fig = figure()
# ax = Axes3D(fig)
# X = np.arange(-4, 4, 0.25)
# Y = np.arange(-4, 4, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# 
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

#pl.show()

normed_subset = count_subset.div(count_subset.sum(1),axis = 0)
normed_subset.plot(kind= 'barh',stacked = True)
#pl.show()










