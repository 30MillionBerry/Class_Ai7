#!/usr/bin/env python
# coding: utf-8

# In[42]:


# list
family = [ 'mom', 'dad', 'dragon', 'pig' ]

## list 의 인덱스 활용
family[0]
family[:4]
family[1:]
family[:2]
family[2][1]
family[-3]


# In[ ]:


## len의 활용 <리스트 안의 원소 갯수 구하기>
len(family)
len(family[:2])

## remove() <리스트 안 원소 지우기> 한번에 하나밖에 못지움
family.remove('pig')           


# In[36]:


## list 특정요소 변경 (그 자리에 있는 값을 다른 값으로 변경)
family
len(family)
family[2] = 'sister'
family


# In[41]:


## list 안에 list
우리는하나 = [['거인', '거인1', '거인2'],['난쟁이1','난쟁이2','난쟁이3'], ['인간1','인간2','인간3']]
len(우리는하나)
우리는하나[0]
우리는하나[0][2]
우리는하나[0][2][2]


# In[141]:


## .append(요소)   list 안에 요소 추가하기
우리는하나.append([['개미']])
우리는하나


# In[148]:


## .insert(위치, 요소)  정해진 위치에 요소 추가하기
우리는하나.insert(0, ['어인1', '어인2'])


# In[165]:


## .extend()    한번에 여러요소 넣기
우리는하나.extend([['외계인1', '외계인2']]) # 리스트안에 리스트를 넣는거면 괄호를 2개 


# In[172]:


## del 리스트명[인덱스]       특정 요소 지우기
del 우리는하나[2][1:]


# In[162]:


## .remove(값)    인덱스가 아니라 값을 지우는 방법
우리는하나.remove([['개미']])


# In[173]:


우리는하나

