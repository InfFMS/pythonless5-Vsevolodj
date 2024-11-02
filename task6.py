# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]
from random import randint
def razvor(list, len):
    a=[]
    for i in range(-1, -1*len-1, -1):
        a.append(list[i])
    return a
n=int(input())
lst=[randint(1, 10) for i in range(n)]
print(lst)
l=lst[:n//2]
r=lst[n//2:]
s = razvor(l, n//2) + razvor(r, n//2)
print(s)