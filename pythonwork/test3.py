# -*- coding: utf-8 -*-
import pandas as pd 

def show_line():
    print "----------------------------------"

unames = ['user_id','gender','age','occupation','zip']

users = pd.read_table('E:\mywork\pythonwork\pydata-book-master\ch02\movielens\users.dat',sep ='::',header=None,names = unames)

rnames = ['user_id','movie_id','rating','timestamp']
#不加双斜杠 会出错
ratings = pd.read_table('E:\\mywork\\pythonwork\\pydata-book-master\\ch02\\movielens\\ratings.dat',sep ='::',header=None,names = rnames)

mnames = ['movie_id','title','genres']

movies = pd.read_table('E:\mywork\pythonwork\pydata-book-master\ch02\movielens\movies.dat',sep ='::',header=None,names = mnames)

print users[:5]
print movies[:5]
print ratings[:5]

#将 users ,ratings,movies 合并为一个表
data = pd.merge(pd.merge(ratings,users),movies)

print data

#性别，计算每部电影的平均得分

#mean_ratings = data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean')
mean_ratings = pd.pivot_table(data,index=['title','gender'],values=['rating'] ,aggfunc='mean',margins=True)

print mean_ratings[:5]

# mean_titile =pd.pivot_table(data,index=['title','gender'],values = ['rating'])
# print mean_titile[:5]

#过滤评分数据不够250条的电影
ratings_by_title = data.groupby('title').size()
show_line()
print ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]
show_line()
print active_titles

mean_ratings = mean_ratings.ix[active_titles]
show_line()
print mean_ratings

#女性喜欢的电影

top_female_ratings =mean_ratings.sort_index(ascending= False)
show_line()
print top_female_ratings[:10]

#根据电影名称分组的得分数据的标准差

rating_std_by_title = data.groupby('title')['rating'].std()
#根据active_titles 进行过滤
rating_std_by_title = rating_std_by_title.ix[active_titles]
# 根据值对series进行降序排序
print rating_std_by_title.order(ascending=False)[:10]


 