#Р-03. Найдите все натуральные числа, принадлежащие отрезку [77 777 777; 88 888 888],
# у которых ровно пять различных нечётных делителей (количество чётных делителей может быть любым).
# В ответе перечислите найденные числа, справа от каждого числа запишите его наименьший нечётный делитель, не равный 1.

#1.Написание функции поиска простого числа
# number = 2^i*m_1^2*m_2
#2.Перебор
#3.Условие для выхода
#4. Проверка основных условий
# number = 1 * m_1 * m_2^2 + m_3^3 + m_4^4
# number = 2^k*m^4
# 20 - 5 * 4

from math import sqrt

def checkPrime(number):
    if number <= 1:
        return False
    delitel = 2
    while delitel * delitel <= number:
        if number % delitel == 0:
            return False
        delitel += 1
    return True

start_num = 77_777_777
end_num = 88_888_888

for i in range(start_num, end_num + 1):
    x = i
    while x % 2 == 0:
        x //= 2
    koren = round(sqrt(sqrt(x)))
    if checkPrime(koren) and koren ** 4 == x:
        print(i, koren)

# 85)(К. Амеличев) Среди целых чисел, принадлежащих числовому отрезку [3661; 33625],
# найдите числа, имеющие ровно один натуральный делитель, не считая единицы и самого числа.
# Ответом будет количество найденных чисел.
start = 3661
end = 33625

def #считает количество делителе1
    return число
count = 0
for i in range(start, end + 1):
    x = i
    d = 2
    if функция(x)== 1 and isinstance(d,int):
          count +=1
print(count)