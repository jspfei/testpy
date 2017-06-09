# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pylab as pl
import numpy as np

names1880 = pd.read_csv('pydata-book-master/ch02/names/yob1880.txt',names = ['name','sex','births'])
print names1880

print names1880.groupby('sex').births.sum()

#将1880-2010所有数据放到 DataFrame里面，并加入year字段， 使用pandas.concat 组合起来

#2010是目前最后一个有效的统计年度

years = range(1880,2011)

pieces = []

columns = ['name','sex','births']

for year in years:
    path  = 'pydata-book-master/ch02/names/yob%d.txt'%year
    frame = pd.read_csv(path,names=columns)
    
    frame['year'] = year
    pieces.append(frame)
    
#将所有数据整合到单个DataFrame中

names = pd.concat(pieces,ignore_index = True)
print names

total_births = names.pivot_table('births',index=['year'],aggfunc=sum)

print total_births.tail()
 
# total_births.plot(title='Total births by sex and year')
#pl.show()

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births/births.sum()
    return group
    
names = names.groupby(['year','sex']).apply(add_prop)
print names
#49
# sex/year组合的前1000个名字

def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]
    
grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
print top1000

boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

# print boys
# print girls

# boys.plot(title='boys')
# pl.show()

total_births = top1000.pivot_table(index=['year','name'],values=['births'],aggfunc = sum)

#print total_births

 

subset = total_births['births']

#subset.plot(subplots=True, figsize=(12,10),grid = False, title="Numer of births per year")
#pl.show()

#评估命名多样性

# table  = top1000.pivot_table(values='prop',index=['year','sex'],aggfunc=sum)
# table.plot(title='sum of table1000.prop by year and sex ',yticks= np.linspace(0,1.2,13),xticks=(1880,2010,10))
# pl.show()

# 最后一个字母的变革
 
get_last_letter = lambda x:x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

table = names.pivot_table(columns=['sex','year','births'],aggfunc = sum)
print table


