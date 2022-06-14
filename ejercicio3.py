from random import random
import matplotlib.pyplot as plt

a=10000000
b=0
lx=[]
ly=[]
for i in range (a):
  x=random()
  y=random()
  if x**2+y**2<1:
    b=b+1
  i=i+1
  if i%10000==0:
    est=4*b/(i)
    lx.append(i)
    ly.append(est)
plt.plot(lx,ly)
plt.show()
