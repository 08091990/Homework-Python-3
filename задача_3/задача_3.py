#В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
#В случае с английским алфавитом очки распределяются так:
#A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. 
#А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. 
#Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
#Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.


a = str(input("Введите слово: "))
print(a)
my_list_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R']
my_list_2 = ['D', 'G']
my_list_3 = ['B', 'C', 'M', 'P']
my_list_4 = ['F', 'H', 'V', 'W', 'Y']
my_list_5 = ['K']
my_list_6 = ['J', 'X']
my_list_7 = ['Q', 'Z']
my_list_8 = ['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
my_list_9 = ['Д', 'К', 'Л', 'М', 'П', 'У']
my_list_10 = ['Б', 'Г', 'Ё', 'Ь', 'Я']
my_list_11 = ['Й', 'Ы']
my_list_12 = ['Ж', 'З', 'Х', 'Ц', 'Ч']
my_list_13 = ['Ш', 'Э', 'Ю']
my_list_14 = ['Ф', 'Щ', 'Ъ']
count = 0
for i in str(a):
    for elem in my_list_1:
        if i == elem:
            count = count + 1
for i in str(a):
    #print(i)
    for elem in my_list_2:
    #print(elem)
        if i == elem:
            count = count + 2
for i in str(a):
    for elem in my_list_3:
        if i == elem:
            count = count + 3
for i in str(a):
    for elem in my_list_4:
        if i == elem:
            count = count + 4
for i in str(a):
    for elem in my_list_5:
        if i == elem:
            count = count + 5
for i in str(a):
    for elem in my_list_6:
        if i == elem:
            count = count + 8
for i in str(a):
    for elem in my_list_7:
        if i == elem:
            count = count + 10 
for i in str(a):
    for elem in my_list_8:
        if i == elem:
            count = count + 1
for i in str(a):
    for elem in my_list_9:
        if i == elem:
            count = count + 2
for i in str(a):
    for elem in my_list_10:
        if i == elem:
            count = count + 3
for i in str(a):
    for elem in my_list_12:
        if i == elem:
            count = count + 5
for i in str(a):
    for elem in my_list_13:
        if i == elem:
            count = count + 8
for i in str(a):
    for elem in my_list_14:
        if i == elem:
            count = count + 10                                                                     
print(count)    
       