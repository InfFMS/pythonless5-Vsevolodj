# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка
from random import randint
def sredsumm(n):
    a = 0
    for i in range(0,N):
        a = a+n[i]
        a = a/len(n)
        return a
N = int(input())
d =[]
s = [0]*N
for i in range(0,N):
    a = randint(0,1000)   #1000
    s[i] = a
print(s)
print(sredsumm(s),sredsumm(s)*1.3, sredsumm(s)/1.3)
for i in range(0,N):
    if s[i] != sredsumm(s)*1.3 and s[i] != sredsumm(s)/1.3:
        d = d+[s[i]]
print(d)


