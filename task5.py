# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.
s=list(map(int, input().split()))
count= 0
max=s[0]
for i in range(len(s)):
    if s[i]==max:
        count+=1
    elif s[i]>max:
        count=1
        max=s[i]
print(count)