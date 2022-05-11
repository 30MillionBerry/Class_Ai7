#!/usr/bin/env python
# coding: utf-8

# # 중복데이터 처리

# ##### Nan 데이터 처리 : dropna(), fillna()
# ##### 중복 데이터 처리 : duplicated(), drop_duplicates()

# In[3]:


import pandas as pd

df = pd.read_excel('./dataset/남북한발전전력량.xlsx')
df.head()


# - ' - '을 Nan으로 변경 후 처리

# In[6]:


import numpy as np
df.replace('-', np.nan, inplace=True)
df.head()


# - 중복데이터를 갖는 데이터프레임 만들기

# In[8]:


df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
df


# - .duplicated()  중복일때부터 True, 중복이기전에는 False

# In[9]:


print(df.duplicated())
print(df['c1'].duplicated())
print(df[['c2','c3']].duplicated())


# - 중복데이터인 경우 삭제 : drop_duplicated()

# In[11]:


print(df.drop_duplicates())    # 행의 모든 값이 중복인 경우 삭제
df.drop_duplicates(subset=['c2','c3'])    # 컬럼 c2 c3 의 값에 대하여


# # 데이터 표준화

# - auto-mpg.csv 파일을 가져옴

# In[18]:


df = pd.read_csv('./dataset/auto-mpg.csv', header=None)


# In[15]:


df


# - column 명 지정

# In[22]:


df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.head()


# - 단위 표준화 : msg( mile per gallon) -> kpl(killometer per liter)
# - 1 mpg = 0.425 km/l

# In[25]:


df['kpl'] = (df['mpg'] * 0.425).round(2)
df.head()

# mpg * 단위를 소수점 2번째까지 짜른 값이 kpl 컬럼이 추가됨


# - as.type('float) => 문자열을 숫자열로 바꿔줌 

# In[40]:


df['horsepower'].replace('?', np.nan, inplace = True)
print(df['horsepower'].unique())
df['horsepower'] = df['horsepower'].astype('float')


# In[36]:


df['horsepower'].dropna(inplace=True)


# In[ ]:


# df.drop(subset=['horsepower'], axis=1, inplace=True)


# In[50]:


df.dropna(subset = ['horsepower'], axis = 0, inplace = True)

df.origin.replace({1 : 'USA', 2 : 'EU', 3 : 'JPN'}, inplace = True)
df.origin = df.origin.astype('category')

print(df['origin'].unique())
print(df['origin'].dtypes)


# In[47]:


# 'model year' -> 정수형의 category로 변경
df['model year'].unique
df['model year'] = df['model year'].astype('category')
df['model year'].sample(10)


# ##### 연습
# - auto-mpg.csv 파일을 읽어와서 df을 생성
# - 컬럼명 부여
# - horsepower 컬럼을 float형으로 형 변환
# - horsepower 에 이상한 값이 있으면 제거

# 1) auto-mpg.csv 파일을 읽어와서 df을 생성

# In[57]:


import pandas as pd
df = pd.read_csv("./dataset/auto-mpg.csv")
df.head()


# 2) 컬럼명 부여

# In[59]:


df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
df.head()


# - 3) horsepower 컬럼을 float형으로 형 변환

# In[66]:


df['horsepower'].replace('?', np.nan, inplace = True)

print(df['horsepower'].unique())
df['horsepower'] = df['horsepower'].astype('float')


# - 4) horsepower 에 이상한 값이 있으면 제거

# In[73]:


# df['horsepower'].dropna(inplace=True)
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)


# In[69]:


df['horsepower'].unique()


# # 범주형(카테고리) 데이터처리

# ### - 구간 분할

# In[74]:


count, bin_label = np.histogram(df.horsepower, bins=3)

bin_names = ['저출력', '보통출력','고출력']
df['hp_bin'] = pd.cut(x = df['horsepower'],    # cut() 함수는 연속데이터를 여러구간으로 나누고 범주형 데이터로 변환
                     bins = bin_label,
                     labels = bin_names,
                     include_lowest=True)


# In[76]:


df.sample(5)


# ### - 더미 변수

# pd.get_dummies()
# - 특성이 존재하면 1 , 아니면 0

# In[77]:


pd.get_dummies(df.origin)


# - 원핫인코딩 one_hot_encoding -> category를 dummy 변수로

# sklearn 의 preprocessing 를 활용한 ont_hot_encoding

# In[78]:


from sklearn import preprocessing as pre


# - 전처리를 위한 encoder 생성

# In[79]:


label_encoder = pre.LabelEncoder()    # label_encoder 생성
onehot_encoder = pre.OneHotEncoder()  # onehot_encoder 생성


# label_encoder 로 문자형 범주를 숫자형 범주로 변경

# In[80]:


onehot_label = label_encoder.fit_transform(df['hp_bin'])
onehot_label


# 2차원으로 변경

# In[82]:


onehot_reshape = onehot_label.reshape(len(onehot_label), 1) # .reshape(변경할 배열, 차원)
onehot_reshape[:10, :]


# 희소 행렬로 변경
# 

# In[ ]:


onehot_fitted = onehot_encoder


# In[ ]:





# # 정규화
# 정규화 -> 값의 범위가 0 ~ 1, 또는 -1 ~ 1 사이의 값으로 변경

# In[85]:


df.horsepower.head()
df_1 = df.copy()


# In[87]:


df_1.horsepower = df_1.horsepower / abs(df_1.horsepower.max())
df_1.horsepower.head()


# 정규화 방법 2 : (최대값 - 최소값) 으로 나누어저 만드는 방법

# In[89]:


df.horsepower = (df.horsepower - df.horsepower.min()) /     (df.horsepower.max() - df.horsepower.min())


# In[90]:


df.horsepower.head(10)


# # 시계열 데이터

# In[96]:


df = pd.read_csv('./dataset/stock-data.csv')
df.head()
df.info()
df.describe()


# Date 컬럼의 값을 object 에서 datetime 형식으로 변경

# In[102]:


df['New_Date'] = pd.to_datetime(df['Date'])
df.info()
df.head()


# New_Date 를 인덱스로, Date 컬럼을 삭제
# 

# In[103]:


df.set_index("New_Date", inplace=True)
df.head()


# In[104]:


df.drop(columns=['Date'], inplace=True) # Date 컬럼 삭제


# In[105]:


df.head()


# 컬럼명을 New_Date -> Date 로 변경

# In[111]:


import pandas as pd

df = pd.read_csv('./dataset/stock-data.csv')
df['New_Date'] = pd.to_datetime(df['Date'])
df.drop(columns = ['Date'], inplace = True)
df.rename(columns = {'New_Date' : 'Date'}, inplace = True)
df.set_index('Date', inplace = True)
df.head()


# In[113]:


import pandas as pd

df = pd.read_csv('./dataset/stock-data.csv')
df['New_Date'] = pd.to_datetime(df['Date'])
df.head()


# new_Date -> datetime : dt.year, dt.month, dt.day

# In[115]:


df['Year'] = df['New_Date'].dt.year
# df['Month'] = df['new_Date'].dt.month
# df['Year'] = df['new_Date'].dt.year
# df['Year'] = df['new_Date'].dt.year
df.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




