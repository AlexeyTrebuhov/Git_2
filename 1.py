# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30.
# То есть: кратно 5 и 10, но не 30. Либо кратно 5 и 15, но не 30.
# PS Иначе все, что кратно 30 - также кратно и 5,10,15. Выигрышных вариантов нет.

import os
os.system("cls")

c = float(input('Введите число, до которого нужно проверить условие кратности числам 5 ,10 и 15 одновременно\n'))
c = int(float(c))

a=0

while a <= c:
    if (a % 5 == 0 and a % 10 == 0 and a % 30 > 0):
        print( 'Число',a, ' кратно 5 и 10, но не 30' )
    if (a % 5 == 0 and a % 15 == 0 and a % 30 > 0):
        print('Число', a, ' кратно 5 и 15, но не 30')
    if (a % 5 == 0 and a % 15 == 0 and a % 30 == 0):
        print('Число', a, 'искомое')
    else:
        print('Число', a, 'выбрано неудачно')
    a+=1