#!/usr/bin/env python
# coding: utf-8

# # 튜플

# - 리스트는 대괄호 , 튜플은 소괄호
# - 리스트는 append를 통해 추가할 수 있지만 튜플은 추가하지 못함
# - 튜플의 핵심은 변하지 않는다

# In[14]:


t1 = (1,2,"a","b")
# del t1[0]

print(t1) # 이렇게 볼 수는 있다

t2 = (3,4)
print(t1 + t2)

a = (1,2)
a = a*3
print(a)


# -----------
# 

# # 딕셔너리

# In[17]:


a = {1: "a"}
print(a)


# - 1.딕셔너리를 Key를 사용해 열기

# In[34]:


ai7 = {1:"양현모", 2:"양창은"}
print(ai7[1])
print(ai7[2])

# 딕셔너리를 넣은 변수에 대괄호열고 키값입력


# - 2.딕셔너리를 추가하고 싶다

# In[21]:


a[2]="b"     
print(a)

# [2]는 키고 "b"는 값이야


# * 3.딕셔너리를 제거하고 싶다

# In[29]:


# del a[3,4]
print(a)

# [] 대괄호 안에 키를 쓰면 딕셔너리 삭제


# - 4.키는 중복되면 안됨 / 벨류는 같아도 됨

# In[35]:


a = {1:"a", 1:"b"}
a

# 겹치면 마지막 키값이 나온다


# * 5.Key만 불러오기 / value 만 불러오기

# In[50]:


a = {1:"a", 2:"b", 3:"c"}
print(a.keys())
print(a.values())

# 변수 뒤에 .keys() 또는 .values()를 붙이면 키,값만 볼 수 있음

for k in a.keys():
    print("키",k)
    
for v in a.values():
    print("벨류",v)


# - 5-1. items
# - items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.

# In[44]:


a.items()


# In[57]:


for k,v in a.items():
    print("키:",k)
    print("벨류:",v)
    
# 소괄호는 튜플, 형태가 변하지 않는다.
# 저 튜플 하나씩 포문장으로인해 반복한다
# 끝나면 다음 차례 다음 차례..


# - 6. clear()  
# 지우기

# In[61]:


test = {1:"q", 2:"w"}
test


# In[62]:


test.clear()


# In[64]:


test
# .clear()


# - 7. get
#             
#       없는 키값을 불러봤다 결과는 에러가 뜬다
#           get을 쓰면 에러가 안나고 None이라고 뜸
#   

# In[96]:


test = {1:"q", 2:"w", "w":"f"}

# print(test[3])  => 에러뜸
print(test.get(3))

# None을 원하는 단어로 바꾸기
test.get(3,"없음") # 3이라는 키가 없기때문에 "없음"을 리턴해라


# - 딕셔너리 안에서 키의 유무 확인방법

# In[99]:


print(3 in test)
print(2 in test)
print(4 in test)
print("w" in test)
print("f" in test) # f 가 있냐고 물었는데 없다함
# 키 in 딕셔너리 형태로만 가능 벨류로는 x


# ---

# 
# # 집합

# - 집합에 관련된 것들을 쉽게 처리하기 위해 만들어진 자료형
# - 중복을 허용하지 않는다
# - 순서가 없다
# 

# In[ ]:


s1 = set([1,2,3]) # 리스트를 set() 라는 함수를 사용하면 집합으로 변함
s1 = {1, 2, 3} # 요롷게 해도됨
print(s1)


# In[107]:


l = [1,2,2,3,3,4,4,5]  # 중복이 많은 리스트가
newList = set(l)  # 중복이 걸러짐
print(newList)

print(list(newList)) # 리스트로 만들기


# In[109]:


s2 = set("hello")
s2 
# "hello"를 집합을 썼더니 
# 집합은 순서가 없다 : 각 객체가 순서없이 뒤죽박죽 되어있음
# 중복을 허용하지 않는다 : ㅣ 이 중복되니 제외됨


# In[113]:


list(s2)
lst_s2 = list(s2)
print(lst_s2)


# ##### 1) 교집합

# In[117]:


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 & s2) 
print(s1.intersection(s2))


# ##### 2) 합집합

# In[119]:


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 | s2)
print(s1.union(s2))


# ##### 3) 차집합

# In[132]:


s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
print(s1 - s2)
print(s1.difference(s2))
print(s2.difference(s1))

a = list(s2.difference(s1)) 
a # 리스트로 만들어보기


# ##### 4) 집합에 추가 / 제거하기 ( add, update, remove ) 

# In[156]:


s1 = set([1,2,3])
s1.add(4)
print(s1)

s1.update([5,6,7]) # 2개 이상은 대괄호
print(s1)

s1.remove(7)
print(s1)


# 
# ---

# # 불

# - 참 : python
# - 참 : [1,2,3] 
# - 참 : 1
# - 거짓 : [], (), {}, ""
# - 거짓 : 0
# - 거짓 : None

# ---

# # 변수

# #####  1) 변수의 주의 사항

# In[162]:


a = [1,2,3]  # [1,2,3] 을 a라는 변수에 넣는다. 
             # [1,2,3] 은 실제 메모리에 저장하고 주소를 갖는다 
             # a도 주소를 들고 있기에 a를 프린트하면 메모리안에 주소를 찾아 불러온다.
        
b = a       # a의 주소를 b에 넣은 것이다.  
print(b)
a[1] = 4    # 인덱스 1번째를 4로 바꾸니
print(b)    # b도 바뀌었다, a와 b가 같은곳을 바라보고있다

print(id(a))
print(id(b)) # 주소가 같다
print(a is b) # 같은 주소냐를 묻는 것


# ##### 2) 복사

# In[164]:


a = [1,2,3]
b = a[:]  # 슬라이싱을 사용해 처음부터 끝까지를 b에 넣는다
a[1] = 4 
print(a)
print(b)

print(id(a))
print(id(b))  # 주소가 다르다


# In[171]:


from copy import copy # copy라는 함수를 가져와야 됨
a = [1,2,3]
b = copy(a) 
a[1] = 4 
print(a)
print(b)

print(id(a))
print(id(b))  # 주소가 다르다


# ##### 3) 할당하는 방법

# In[ ]:


a, b = 'gomugomu', 2  # 소괄호로 묶였으니 튜플, 괄호를 왼쪽이든 오른쪽이든 상관없음 
                        # 둘다 묶여도 상관 없음 괄호가 없어도됨
print(a)
print(b)

(e, f) = 3,4
print(e)
print(f)


c, d = [1, 2] # 대괄호로 묶어도 됨
print(c)
print(d)

[h,i] = 5,6
print(h)
print(i)


# In[182]:


v = s = 'hello'
print(v)
print(s)
print(id(v))  # 주소가 같네?
print(id(s))


# In[184]:


# 바꾸는 기술
a = 3
b = 5
a,b = b,a 

print(a)
print(b)

