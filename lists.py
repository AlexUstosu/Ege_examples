#39)	Найдите основание системы счисления, в которой выполнено умножение: 3·213 = 1043.
# def convert_to_decimal(number_str, base):
#     # перевод строки в 10-ю СС
#     decimal_number = 0
#     power = 1  # Начинаем с 1 (N^0)
#
#     for digit in reversed(number_str):
#         decimal_number += int(digit) * power
#         power *= base  # Увеличиваем степень основания
#
#     return decimal_number
#
# for N in range(4, 20):  # Начнем с 4, так как у нас есть цифра '3'
#     a = 3
#     b = convert_to_decimal('213', N)
#     c = convert_to_decimal('1043', N)
#
#     if a * b == c:
#         print(N)
#
#
# #1 - возвращаемые
# def f():
#     return 'Monday'
#
# number = 5
#
# #2 - принимаемые
# def f_1(power):
#     global number
#     number = number ** power
#
# #2 - и принимаемые и возвращаемые
# def f_2(number, power):
#     number = number ** power
#     return number
#
# f_1(3)
#
# print(number)



N = int(input("Введите целое число: "))

if N < 2:
    print("Error")
else:
    array = [1, 2, 8, 0, 3, -9, -6, 12]

    #Удаление
    array.remove(12)
    print(array)

    array.pop(0)
    print(array)

    #Добавление
    array.append(100)
    print(array)
    array.extend([101, 102, 103, 104, 105, 106])
    print(array)
    array.insert(3,257)
    print(array)

    #Сортировка
    array.sort()
    print(array)

    array.sort(reverse= True)
    print(array)

    array.reverse()
    print(array)

    print(reversed(array))

    array.count(3)       #кол-во элементов
    array.clear()        #очистка
    array.copy()

    array1 = array              #поверхностная копия
    array2 = array.copy()       #глубокая копия

    print(array)

    min_v = min(array)

    max_v = max(array)

    array.remove(min_v)
    array.remove(max_v)

    print(array)
    summ = sum(array)



print(summ / (N - 2))


