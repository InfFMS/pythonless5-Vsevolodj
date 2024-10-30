# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.
from random import randint
def identical3znach(N):
    a = []
    b = 1
    while N >=10:
        a = a + [N%10]
        N = N//10
    a += [N]
    for j in range(len(a)-1):
        if a[j] != a[j+1] and 99<a[j]<1000:
            b = b*0
        else: b = b*1
    return b
N = int(input())
s = [0]*N
c =1
for i in range(0,N):
    a = randint(0,1000)
    s[i] = a
print(len(s))
print(s[-1])
print(s[::-1])
for j in range(N):
    if identical3znach(s[j]) ==1:
        c=c*1
    else: c=c*0
if c ==1 :
    print("YES")
else: print("NO")
print(s[1:-1])
