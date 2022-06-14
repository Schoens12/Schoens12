#numeros aleatorios 
import random 
lista=[] 
for i in range(20): 
  lista.append(random.uniform(1, 1000)) 
print lista 

#promedio de numeros aleatorios 
import random 
lista=[] 
for i in range(20): 
  lista.append(random.uniform(1, 50)) 
print lista 
print lista[10:20] 
print 'promedio = ',sum(lista[10:20])/(len(lista)/2)
