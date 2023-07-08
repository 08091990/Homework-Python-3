#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

N = int(input("Введите число N: "))
import random
array = [] 
for i in range(N):
    array.append(random.randint(1, N)) 
print(array) 
b = int(input("Введите число из массива: "))
index = 0
nearest_value = array[0] 
min_difference = abs(array[i] - b)
for i in range(N):
    difference = abs(array[i] - b)
    if difference < min_difference:
        min_difference = difference
        nearest_value = array[i]
        index = i
print(f"Ближайшее значение: {nearest_value}")



