# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]
from random import randint
def identical(N):
    a = []
    b = 1
    while N >=10:
        a = a + [N%10]
        N = N//10
    a += [N]
    for j in range(len(a)-1):
        if a[j] != a[j+1]:
            b = b*0
        else: b = b*1
    return b
N = int(input())
s=[]
a = []
for i in range(0,N):
    value = randint(10,100000)
    s = s+[value]
for k in range(0,len(s)):
    if identical(s[k])== 1:
        a = a+[s[k]]
print(a)

