#!/usr/bin/env python
# coding: utf-8

# # 데이터프레임 합치기

# - pd.concat(데이터프레임 리스트)

# In[1]:


import pandas as pd


# In[2]:


df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index=[0, 1, 2, 3])
 
df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index=[2, 3, 4, 5])


# In[3]:


print(df1)
print(df2)


# 
# 
# --------------------------------------------------------------

# ### - concat

# In[13]:


print(pd.concat([df1, df2]))   # 행으로 데이터프레임 연결하기
print(pd.concat([df1, df2], ignore_index=True))  # 기존의 인덱스 무시


# In[14]:


pd.concat([df1, df2], axis=1)  # 컬럼으로 연결하기


# In[18]:


print(pd.concat([df1,df2], axis=0, join='inner'))   # 인덱스가 같은 행만 join
print(pd.concat([df1,df2], axis=1, join='inner'))   # 컬럼으로 붙인다

# 아래와 위를 잘 비교하삼


# In[21]:


# 데이터 프레임과 시리즈 연결
sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')


# In[27]:


print(sr1)
print(sr2)
print(sr3)


# In[30]:


print(pd.concat([df1, sr1], axis=1))   # 데이터프레임 df1과 시리즈 sr1을 컬럼으로 엮는다

print()
print(pd.concat([df2, sr2], axis=0))


# In[31]:


# sr, df, join='outer' -> 'inner', axis=0 (아래로 연결), axis=1 (옆으로 연결)
# pd.concat([])
pd.concat([sr1,sr2,sr3], axis=1) 


# ## merge

# - pd.merge( left, right, how=, on=)

# In[39]:


df1 = pd.read_excel('dataset/stock_price.xlsx')
df2 = pd.read_excel('dataset/stock_valuation.xlsx')

print(df1.head())   # id---stock_name---value---price
print()
print(df2.head())      # id---name---eps-bps-per-pbr


# In[37]:


merge_inner = pd.merge(df1, df2, how='left')
merge_inner


# In[40]:


pd.merge(df1, df2, how='outer')  # how = 'right' => df2는 모두 추출


# In[41]:


pd.merge(df1, df2, how='inner', on='id')    # on=컬럼명, 특정 컬럼의 값을 기준


# In[44]:


pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')


# In[48]:


# price 가 50000 미만인 자료의 id, name, value, price, eps, bps, per 를 추출
# 1. df1 에서 price가 50000 미만인 자료의 id, value, price 만 추출
price = df1.loc[df1['price']<50000,['id','value', 'price']]
print(price)
# 2. df1 과 df2 (name-eps-bps-per 만 가져와서) merge
df_2 = df2.loc[:, ['id','name','eps','bps','per']]
df_2

pd.merge(price, df_2, how='left')


# In[49]:


# df1.join(df2) 인덱스를 기준으로 조인
# index를 생성
df3 = df1.set_index('id')
df4 = df2.set_index('id')
df3.head()


# In[50]:


df3.join(df4)


# In[ ]:


df1.join(df2)


# - how = 'left' => 옵션을 설정하면 왼쪽 데이터프레임의 키 열에 속하는 데이터 값을 기준으로 병합
# - left_on 과 right_on 옵션으로 좌우 데이터프레임에 각각 다르게 키를 정할 수 있음
# - how = 'outer' => 기준이 되는 열의 데이터가 데이터프레임 중 어느 한쪽에만 속하더라도 포함한다는 뜻
# - how = 'inner' => 기준이 되는 열의 데이터가 양쪽 데이터프레임에 공통으로 존재하는 교집합일 경우만 추출
# - on = None => 두 데이터 프레임에 공통으로 속하는 모든 열을 기준(키)으로 병합

# In[51]:


# 그룹연산
# 'titanic' 에서 'age', 'sex', 'class', 'fare', 'survived' 컬럼만 가져옴
import seaborn as sns
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['age', 'sex', 'class', 'fare', 'survived']]
df.head()


# In[ ]:


# 그룹 연산 실행 순서
# 1. 데이터를 특정 조건으로 분할
# 2. 분할된 데이터를 집계, 변환, 필터링
# 3. 2단계에서 실행된 결과를 결합


# In[52]:


print(df['class'].unique())
# df.groupby(컬럼명)
grouped = df.groupby('class')


# In[53]:


for key, group in grouped:
    print("key : ", key)
    print(group.head())


# In[54]:


grouped.mean()   # 그룹별 각 컬럼의 평균


# In[55]:


# First 클래스의 승객막 추출
grouped.get_group("First")


# In[64]:


# 'class'로 그룹을 지은 뒤 각 클래스별 가장 많은 나이를 추출
class_group = df.groupby('class')
class_group['age'].max() 


# In[68]:


# class, sex를 기준으로 그룹을 짓고 각 그룹의 자료를 출력
class_sex = df.groupby(['class','sex'])
for key, group in class_sex:
    print("key: ", key)
    print("number : ", len(group))
    print(group.head())


# In[69]:


# 각 클래스별 성별 나이, 요금, 생존율의 평균
class_sex[['age','fare','survived']].mean()


# In[ ]:





# In[70]:


# 3등석의 male의 자료만 추출
class_sex.get_group(('Third', 'male'))['age'].min()


# In[77]:


# auto-mpg.csv 파일을 origin 을 1 : USA, 2 : EU, 3 : JPN
# 제조 국가별로 mpg의 평균
# USA 의 weight 가 가장 작은 값을 추출

import pandas as pd
import numpy as np

df = pd.read_csv("dataset/auto-mpg.csv", header=None)


# In[79]:


df.columns =  ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.head()


# In[81]:


df.origin.replace({1:'USA', 2:'EU', 3:'JPN'}, inplace=True)


# In[83]:


df.head()


# In[88]:


class_origin = df.groupby('origin')
class_origin['mpg'].mean()


# In[89]:


# USA 의 weight 가 가장 작은 값을 추출
# class_sex.get_group(('Third', 'male'))['age'].min()
class_origin.get_group('USA')['weight'].min()


# In[90]:


# class_sex[['age','fare','survived']].mean()
class_origin[['weight']].min()


# In[ ]:


# 그룹 메서드 -> grouped.컬럼.그룹함수()


# In[92]:


import seaborn as sns
titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['age', 'sex', 'class', 'fare', 'survived']]


# In[93]:


grouped = df.groupby('class')
grouped.fare.std()


# In[100]:


# 매핑함수를 여러 개
def min_max(x):
    return x.max() - x.min()

grouped.agg(min_max)


# In[101]:


grouped.agg([min, max])


# In[102]:


grouped[['age','fare']].agg([min, max])  


# In[103]:


grouped.agg({'age':['min','max'], 'fare':['mean']})


# In[104]:


df.groupby('sex').agg(['min','max','sum','count'])


# ---------------------------------------------------------------------------------------------

# # 그룹연산

# In[111]:


df.age.unique()


# In[113]:


df = titanic.loc[ : , ['age', 'class', 'fare', 'survived']]
groupby = 
df.age.fillna(0, inplcae=True)


# In[118]:


# 그룹 연산 데이터 변환 : 값 - 평균(키) / 표준편차(키)
age_mean = grouped.age.mean()
print(age_mean)

age_std = grouped.age.std()
print(age_std)

for key, group in grouped:
    group_score = (group['age'] - age_mean.loc[key]) / age_std.loc[key]
    print("key : ", key)
    print(group_score.head(3))

print()
print()

# transform() : 그룹의 각 원소에 그룹함수를 적용
def group_score(x):
    return (x - x.mean())/ x.std()

age_score = grouped.age.transform(group_score)
print(age_score.loc[[1,9,0]])


# In[116]:


age_score = grouped.age.transform(lambda x : (x - x.mean())/ x.std())
print(age_score.loc[[1,9,0]])


# In[122]:


# class, age, fare 컬럼을 가지고 와서 sex로 그룹을 나누고
df1 = titanic.loc[ : ,['class','age', 'fare']]
# 그룹별로 자신의 fare에 자기가 속한 그룹의 fare의 평균값을 뺀 값을 구하세여
df1_fare = df1.groupby('class').fare.transform(lambda x : x- x.mean())
# 1, 9, 0 인덱스를 가져와서 출력
df1_fare[[1, 9, 0]]


# In[124]:


# 그룹 객체 필터링 filter 함수 : 그룹객체.filter(조건식 함수)
df1_grouped = df1.groupby('class')
df1_result = df1_grouped.filter(lambda x : len(x)>=200)
df1_result['class'].unique()


# In[126]:


# 평균나이가 30보다 작은 그룹의 데이터만 출력
df_grouped.filter(lambda x : x.age.mean() < 30)['class'].unique())


# In[128]:


# 그룹객체에 함수 매핑 : 그룹객체.apply(매핑함수)
df1_grouped.apply(lambda x : x.describe())


# In[131]:


df1_grouped.age.apply(lambda x : x - (x.mean())/x.std())


# In[132]:


age_filter = df1_grouped.apply(lambda x : x.age.mean()<30)
for key in age_filter.index:
    if age_filter[key] == True:
        age_filter_df = df1_grouped.get_group(key)
        print(age_filter_df.head())


# In[136]:


# titanic 에서 'sex', 'age', 'class', 'fare', 'survived' 컬럼을 가져옴
import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df_2 = titanic.loc[ : , ['sex', 'age', 'class', 'fare', 'survived']]

df_2_grouped = df_2.groupby(['class', 'sex'])
gdf = df_2_grouped.mean()
gdf


# In[138]:


gdf.loc[('First', 'female')]  # 처ㅡㅁ 인덱스를 기준으로 추출 (인덱스1, 인덱스2)


# In[139]:


# 두번째 인덱스를 기준으로 데이터를 검색:
# 그룹객체.xs(그룹의 값, level=그룹명)
# sex == 'male'인 자료 검색
gdf.xs('male', level='sex')


# In[155]:


# 피벗 : pd.pivot_table()
df2

pdf = pd.pivot_table(df_2,
               index=['class','sex'],
               columns=['sex','survived'],
               values=['age', 'fare'],
               aggfunc=['mean','sum'])


# In[156]:


pdf


# In[157]:


pdf.xs(0, level='survived', axis=1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




