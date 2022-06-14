#beta
import random 
import matplotlib.pyplot as plt 
num = [] 
m = 10
s = 5 
for i in range(10000): 
  temp = random.betavariate(m,s) 
  nums.append(temp) 
plt.hist(nums, bins = 100, color= "blue") 
plt.show() 

#triangular
import random 
import matplotlib.pyplot as plt 
num = [] 
m = 10
s = 5 
for i in range(10000): 
  temp = random.triangular(m,s) 
  nums.append(temp) 
plt.hist(nums, bins = 100, color= "blue") 
plt.show() 

#paretovariate
import random 
import matplotlib.pyplot as plt 
num = [] 
m = 10
s = 5 
for i in range(10000): 
  temp = random.paretovariate(m,s) 
  nums.append(temp) 
plt.hist(nums, bins = 100, color= "blue") 
plt.show() 

#se repite para cada una de las solicitadas
