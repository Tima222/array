#Вычислить среднее арифметическое положительных элементов массива F(M).
a=[int(i) for i in input().split()] #Задаём массив
counter1=0
counter2=0
for i in a:
    if i>0:
        counter1+=i
        counter2+=1
print(counter1/counter2)
