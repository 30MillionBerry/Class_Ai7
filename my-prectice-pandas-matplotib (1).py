#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_excel("./dataset/시도별 전출입 인구수.xlsx")

df.head()
# df.info() 


# ### .fillna(method='ffill')
# 누락된 데이터 처리 : 누락 데이터(Nan) -> 이전 값으로 대체

# In[6]:


df = df.fillna(method='ffill')
df.head()


# ####    서울에서 다른 지역으로 전출한 인구의 분포도 확인
# ####    '전출지별' 컬럼의 값이 '서울특별시'인 자료만 추출

# In[15]:


df_seoul = df[ (df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')]
# df_seoul = df[mask]
df_seoul


# #### '전출지별' 컬럼삭제

# In[16]:


df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.head()


# #### '전입지별' 컬럼명을  '전입지'로 변경
# 

# In[19]:


df_seoul.rename( {'전입지별' : '전입지'}, axis=1, inplace=True)
df_seoul.head()


# #### '전입지' 컬럼을 인덱스로

# In[20]:


df_seoul.set_index('전입지', inplace=True)


# In[21]:


df_seoul.head()


# #### 전입지가 경기도인 자료만 추출 sr_one 에 저장
# 

# In[105]:


sr_one = df_seoul.loc['경기도']   # 시리즈 반환


# ### 그래프 그리기
# sr_one 인덱스를 x축
# 
# sr_one 의 값을 y 값으로 

# In[24]:


plt.plot(sr_one.index, sr_one.values)         # plt.plot(x,index, x.values)


# #### 그래프의 제목추가
# 서울 -> 경기도 인구이동

# In[33]:


from matplotlib import font_manager, rc
font_path = './dataset/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


# In[34]:


plt.title('서울 -> 경기도 인구 이동')
plt.plot(sr_one)


# #### x 라벨명, y 라벨명 추가

# In[37]:


plt.title('서울 -> 경기도 인구 이동')
plt.xlabel('기간')
plt.ylabel('인구수')
plt.plot(sr_one)


# In[58]:


# 그래프 사이즈 지정
plt.figure(figsize=(14,5))
plt.plot(sr_one, marker= 'o',color='blue', markerfacecolor='red') # 그림을 그려놓고 밑에 계속 추가// 마커 추가

plt.title('서울 -> 경기도 인구 이동')
plt.xlabel('기간')
plt.ylabel('인구수')


# plt.xticks(rotation='vertical')  # xticks 의 내용을 수직으로 보여줌
plt.xticks(rotation=70, size=12)

# 라벨 붙이기// 내용과 위치 사이즈
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=12)

# y축 범위 지정 (최소값, 최대값)
plt.ylim(50000, 800000)


# ### 화살표 주석표시

# In[76]:


# 그래프 사이즈 지정
plt.figure(figsize=(14,5))
plt.plot(sr_one, marker= 'o',color='blue', markerfacecolor='red') # 그림을 그려놓고 밑에 계속 추가// 마커 추가

plt.title('서울 -> 경기도 인구 이동')
plt.xlabel('기간')
plt.ylabel('인구수')


# plt.xticks(rotation='vertical')  # xticks 의 내용을 수직으로 보여줌
plt.xticks(rotation=70, size=12)

# 라벨 붙이기// 내용과 위치 사이즈
plt.legend(labels=['서울 -> 경기'], loc='best', fontsize=12)

# y축 범위 지정 (최소값, 최대값)
plt.ylim(50000, 800000)

# 주석 표시 - 화살표
plt.annotate('',
             xy=(20, 620000),       #화살표의 머리 부분(끝점)
             xytext=(2, 290000),    #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5), #화살표 서식
             )

plt.annotate('',
             xy=(47, 450000),       #화살표의 머리 부분(끝점)
             xytext=(30, 580000),   #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),  #화살표 서식
             )

# 주석 표시 - 텍스트
plt.annotate('인구이동 증가(1970-1995)',  #텍스트 입력
             xy=(10, 400000),            #텍스트 위치 기준점
             rotation=25,                #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.annotate('인구이동 감소(1995-2017)',  #텍스트 입력
             xy=(40, 500000),            #텍스트 위치 기준점
             rotation=-10,               #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.show()        # Text 안보이게


# ### 한 화면에 그래프 여러개 그리기

# In[107]:


fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2, 2, 1)  # 1행에 2개, 1열에 1개의 그래프를, 그중 1개 그래프다
ax2 = fig.add_subplot(2, 2, 2)  # 1행에 2개, 1열에 1개의 그래프를, 그중 2개 그래프다
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)

# axe 객체에 plot()
ax1.plot(sr_one, marker='o')
ax2.plot(sr_one, marker='*', label='서울-> 경기')
ax2.legend(loc='best')
ax3.plot(df_seoul.loc['강원도'], color='red')
ax4.plot(df_seoul.loc['충청북도'],color='black')


ax3.set_title('서울 -> 강원도')
ax4.set_title('서울 -> 충청북도')
ax1.set_ylim(50000, 800000)
ax2.set_ylim(50000, 800000)

ax1.set_xticks(sr_one.index)
ax2.set_xticks(sr_one.index)

ax1.set_title('ax1')
ax2.set_title('ax2')


plt.show()


# #### 한 화면의 한 axe 에 그래프 여러개 그리기
# 전출지가 충청남도, 경상북도, 강원도인 자료를 가져옴

# In[99]:


df_seoul.columns
print()
# col_years = list(map(str, range(1970, 2018)))  # 컬럼명을 생성
col_years = list(map(str, range(1970, 2018)))

# df_1 = df_seoul.loc[ ['충청남도', '경상북도', '강원도' ], col_yearsabs]
df_1 = df_seoul.loc[ ['충청남도', '경상북도', '강원도' ], :]
df_1


# In[109]:


fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(1,1,1)

ax.plot(col_years, df_1.loc['충청남도', :], label='서울->충남')
ax.plot(col_years, df_1.loc['경상북도', :], label='서울->경북')
ax.plot(col_years, df_1.loc['강원도', :], label='서울->강원')
ax.legend(loc='best')

ax.set_title('서울->충남, 경북, 강원 인구이동', size=20)
ax.set_xlabel('기간')
ax.set_ylabel('이동 인구수')
ax.set_xticks(col_years)
ax.tick_params(axis='x', labelrotation=75)

plt.show()


# ### area 그리기

# In[120]:


# 기간을 인덱스로 인덱스를 컬럼으로
df_1 
df_2 = df_1.T

# 기간을 정수 인덱스로 변경
df_2.index = df_2.index.map(int)
df_2.index
df_2.plot(kind='area', stacked=True, alpha=0.3)


# ### 막대 그래프

# In[123]:


df_3 = df_1.copy()
df_3
# df_3['합계'] = df_3.sum(axis)


# In[126]:


# 2010년부터 2017년까지의 인구이동수를 막대 그래프로

df_seoul  # '충청남도', '경상북도', '강원도' 만 추출
col_years = list(map(str, range(2010, 2018)))

df_3 = df_seoul.loc[ ['충청남도', '경상북도', '강원도'], col_years]
df_3

# indexd와 칼럼의 위치 변경 : transpose()
df_3 = df_3.T


# In[127]:


df_3.plot(kind='bar', figsize=(20, 5))


# In[128]:


df_3 = df_3.T
# '합계' 컬럼 추가
df_3['합계'] = df_3.sum(axis=1)
df_3.plot(kind='barh', figsize=(20, 5))


# ### twins()
# x축은 같고 y축의 값이 다른 두 개의 그래프를 하나의 ax에 그리기

# In[150]:


df = pd.read_excel("./dataset/남북한발전전력량.xlsx")
df


# ###### 북한의 자료만 추출

# In[151]:


df_ns = df.loc[5:, :]     # df.loc[ 5: ] = 동일한 결과
df_ns.columns[0]


# ###### '전력량 (억kwh)' 컬럼삭제
# 

# In[152]:


df_ns = df_ns.drop('전력량 (억㎾h)', axis='columns')


# #### index 를 '발전 전력별' 로 변경

# In[153]:


df_ns.set_index(df_ns.columns[0], inplace = True)


# In[154]:


df_ns = df_ns.T
df_ns


# In[165]:


# 년도별 발전량의 종감율
# 합계 -> 총발전량, 이전 년도와 올해 총발전량의 차이 -> 종강율
# "이전 년도 발전량" => df_ns['총발전량']
df_ns['이전년도 발전량'] = df_ns['총발전량'].shift(1)
df_ns.head
# 종감율 : (총발전량 / "총발전량-1년") -1 ) * 100
# ( (263/277)-1) * 100
df_ns['증감율'] = ((df_ns['총발전량'] / df_ns['이전년도 발전량'])-1) * 100
df_ns.head()


# In[155]:


df_ns.rename(columns={"합계" : "총발전량"}, inplace=True)
df_ns


# pd.Series([2,3,4,5]).shift(1).shift(1)  # 하니씩 밀림

# ### '수력' 과 '화력' 자료만 bar로 그래프 그림
# ### 위의 그래프에 증감율을 추가해서 그리기

# In[171]:


# 폰트지원
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname = './dataset/malgun.ttf').get_name()
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

ax1 = df_ns[ ['수력', '화력']].plot(kind='bar', figsize=(20,6), stacked=True)
ax2 = ax1.twinx()
ax2.plot(df_ns.index, df_ns['증감율'], ls='--', marker='o', markersize=8,
        color='red', label='전년대비 증감율(%)')
ax1.set_ylim(0, 400)
ax2.set_ylim(-50, 50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량 (억Kwh)')
ax2.set_ylabel('전년 대비 증감율(%)')

plt.title('북한 전력 발전량 (1990 - 2016)', size=30)
ax1.legend(loc='upper left')

plt.show()


# # seaborn 그래프 그리기

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

titanic = sns.load_dataset('titanic')


fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)


# ### sns.그래프함수(x=컬럼, y=컬럼, data=df, ax=ax1)

# In[173]:


sns.regplot(x='age', y='fare', data=titanic, ax=ax1)
sns.regplot(x='age', y='fare', data=titanic, ax=ax2, fit_reg=False)
plt.show()


# In[175]:


# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import matplotlib.pyplot as plt
import seaborn as sns
 
# Seaborn 제공 데이터셋 가져오기
titanic = sns.load_dataset('titanic')
 
# 스타일 테마 설정 (5가지: darkgrid, whitegrid, dark, white, ticks)
sns.set_style('darkgrid')

# 피벗테이블로 범주형 변수를 각각 행, 열로 재구분하여 정리
table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')

# 히트맵 그리기
sns.heatmap(table,                  # 데이터프레임
            annot=True, fmt='d',    # 데이터 값 표시 여부, 정수형 포맷
            cmap='YlGnBu',          # 컬러 맵
            linewidth=.5,           # 구분 선
            cbar=True)             # 컬러 바 표시 여부

plt.show()


# In[183]:


get_ipython().system('pip install folium')
import folium


# In[ ]:


seoul_map = 


# In[180]:


# 대학교 리스트를 데이터프레임 변환
df = pd.read_excel('./dataset/서울지역 대학교 위치.xlsx', engine= 'openpyxl')
df.head()
df_set_index(df.columns[0], inplace=True)


# In[186]:


df.set_index(df.columns[0], inplace = True)

# 서울 지도 만들기
seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', 
                        zoom_start=12)

# 대학교 위치정보를 Marker로 표시
for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat, lng], popup=name).add_to(seoul_map)

# 지도를 HTML 파일로 저장하기
seoul_map.save('./dataset/seoul_colleges.html')

