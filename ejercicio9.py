import random
import numpy as np
List = ['Tula','Mnazanillo','Merida','Cuerna','Ciudad de México','Rio','Mexicali','Madrid']
random.shuffle(List)
City = random.choice(List) 
print ("La ciudad elegida es :",City)

city2 = random.sample (list, 3)
print ("Las ciudades al azar son", city2)
