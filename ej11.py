import random
import numpy as np
import matplotlib.pyplot as plt   

num = []
p=0.5

for i in range(10000):
    x=random.random()
    if x<=(1-p):
      y=0
    else:
      y=1
    nums.append(y)

plt.hist(num, bins = 15, color = 'blue')
plt.show()
