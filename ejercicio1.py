from cmath import sqrt
import random as rd

print('Ejercicio 1, volado\na)')

x = rd.random()

if x < .5:
    print('El resultado es sol')
else:
    print('El resultado es aguila')

print('b) ')

s=0
a=0

for i in range(1000):

    x = rd.random()

    if x < .5:
        s+=1
    else:
        a+=1

print('La probabilidad de que caiga sol en un volado es de ' + str((s/1000)*100) + '%')
