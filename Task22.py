'''
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств
'''

from random import randint

length_1, length_2 = int(input('Enter numbers of length of two sets with "ENTER": ')), int(input('2-nd: '))

input_set_1 = set(randint(-16, 31) for _ in range(length_1)) # Создаю 2 рандомных множества
input_set_2 = set(randint(-16, 31) for _ in range(length_2))

output_numbers = sorted(list(input_set_1 & input_set_2)) # output_numbers = work_set_1.intersection(work_set_2)
                                    #Пересечение множеств (только те элементы, которые есть в обоих множествах)      
                          #Преобразую в список
                    #Сортирую по возрастанию
print(output_numbers)