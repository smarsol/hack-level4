
def mitjana(nums):
  N = 0
  for i in nums:
    N += i
  return(N/len(nums)) 


def variancia(nums):
  N = 0
  for i in nums:
    N += (i - mitjana(nums))**2
  return(N/len(nums))

column1 = []
column2 = []

with open('data2.txt', 'r') as f:
  for line in f:
    if line[-1] == '\n': 
        print(line[:-1]) 
    else: 
        print(line) 
    mylist  = line.split()
    num1 = int(mylist[0])
    num2 = int(mylist[1])
    column1.append(num1)
    column2.append(num2)
     
print(column1)
print(column2)

m_1 = mitjana(column1)
v_1 = variancia(column1)
m_2 = mitjana(column2)
v_2 = variancia(column2)

print(m_1)
print(v_1)
print(m_2)
print(v_2)

import numpy as np
nums = np.random.randn(1000)
print(mitjana(nums))
print(variancia(nums))
