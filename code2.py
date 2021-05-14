#Определить сумму элементов массива N(M), кратных трем.

a=[int(i) for i in input().split()]
counter=0
for i in a:
    if i%3==0:
        counter+=i
print(counter)
