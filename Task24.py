'''
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. 
Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло 
различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
'''
bushes = int(input('Enter the number of bushes: '))
berries = list(int(input('Enter the numbers of berries on the bush: ')) for _ in range(bushes))
maximum, temp = 0, 0
for i in range(len(berries)):
    if i == 0:
        temp = sum(berries[:2]) + berries[-1]
    elif i == len(berries) - 1:
        temp = sum(berries[-2:]) + berries[0]
    #if berries[i] == berries[0]:
        #temp = sum(berries[:2]) + berries[-1]
    #elif berries[i] == berries[-1]:
        #temp = sum(berries[-2:]) + berries[0]
    else:
        temp = sum(berries[i-1:i+2])
    if temp > maximum:
        maximum = temp
print(f'The maximum possible number of berries: {maximum}')

