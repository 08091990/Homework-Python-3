#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X


import random
N = int(input("Введите число N: ")) 
a = [0]*N
for i in range(N):
    a[i] = random.randint(1, N)
    print(a)
x = int(input("Введите число x: "))
b = 0
for i in range(N):
    if a[i] == x:
        b += 1
    print(b)