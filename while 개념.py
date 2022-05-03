#!/usr/bin/env python
# coding: utf-8

# In[1]:


# while 반복문
num = 1               # ~하는 동안에
while num <= 100 :  #while은 어떤 조건이 만족되는 동안 그 아래에 쓴 문장들을 반복하는 기능을 갖고 있음. 
                    #여기서는 num이 100 이 될 때까지 print(num)과 num = num + 1을 반복하는 것
    print(num)
    num += 1


# In[ ]:


# input()으로 사용자로부터 정수를 한 개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요. 
# 이때 출력 앞에 공백을 한 칸 주어서, 입력과 출력이 구분되게 합니다.

num = int(input())  # input()은 문자열로 입력되므로 숫자를 원한다면 정수형으로 변환해야함

i = 1               # i라는 변수에 1을 할당한다
while i <= num:     # 사용자가 입력한 숫자가 1보다 크거나 같으면   # 다시반복) 2가 숫자보다 작거나 같으면..
    print('', num)   #  숫자를 출력하고
    i += 1           # i 에 1을 더하고 변수에 저장


# In[ ]:


# 정수를 한 개 입력받아, 
# 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프린트하는 프로그램을 작성해 보세요. 
#단, while 문을 사용하세요.

num = int(input())     # input 값을 정수화하여 num 에 할당

i = 1                  # 1을 i 변수에 할당

while i <= num:       # i가 num(인풋값)보다 작거나 같을시 반복 # 2(i) 가 ..!#@
    print(i, i * i)    # i , i, i * i 를 출력
    i = i + 1          # 조건문을 충족했으니 i 에 1을 더한 값을 변수에 할당 후 다시 9열로 가서 실행


# In[14]:


# 고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다. 
# 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.



high = 100
i = 1

while i <=10 :
    high *= 3/5
    print(high)
    i += 1


# In[15]:


number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10      # rem = 8 #  rem =5    # 3
    rev = rev * 10 + rem   # rev = 8 # rev= 85    # 853
    number = number // 10  # numver = 35 num=3    # 0

print(rev)

