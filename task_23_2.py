# B = {i for i in range(35,76)}
# C = {i for i in range(60,111)}
# A = set()
# for x in range(120):
#
#     expression = (x not in A) <= ((x in B) == (x in C))



#176)Исполнитель Калькулятор преобразует число, записанное на экране. У исполнителя есть три команды, которым присвоены номера:
# 1. Прибавь 1
# 2. Прибавь 2
# 3. Умножь на 3
# Первая команда увеличивает число на экране на 1, вторая увеличивает
# его на 2, третья – умножает на 3. Программа для исполнителя – это последовательность
# команд. Сколько существует программ, которые преобразуют исходное число 2 в число 38,
# и при этом траектория вычислений содержит числа 15 и 30, а также не содержит чисел 12 и 20.
# Также программа не должна содержать двух команд «Умножь на 3» подряд.

#1243550
# from functools import *
#
# @lru_cache(None)
# def f(start_number, result_number, last_command, flag_15, flag_30):
#     if start_number == 15:
#         flag_15 = 1
#     if start_number > 15 and flag_15 == 0:
#         return 0
#
#     if start_number == 30:
#         flag_30 = 1
#     if start_number > 30 and flag_30 == 0:
#         return 0
#
#     if start_number > result_number or start_number == 12 or start_number == 20:
#         return 0
#     elif start_number == result_number:
#         return 1
#     else:
#         if last_command == "*3":
#             return f(start_number + 1, result_number, "+1", flag_15, flag_30) + f(start_number + 2, result_number, "+2", flag_15, flag_30)
#         else:
#             return f(start_number + 1, result_number, "+1", flag_15, flag_30) + f(start_number + 2, result_number, "+2", flag_15, flag_30) + f(start_number * 3, result_number, "*3", flag_15, flag_30)
# print(f(2,38,"", 0, 0))

#181)(А. Брейк) Непоседливый Непоседа решил сыграть в игру. Он придумал исполнителя, преобразующего числа на доске и имеющего три команды:
# 1. Вычесть 1
# 2. Вычесть 2
# 3. Извлечь корень
# Первые две команды уменьшают число на доске на 1 и 2 соответственно, третья команда — извлекает
# из числа квадратный корень, если число является квадратом любого числа. Программа для такого исполнителя —
# это последовательность команд. Сколько различных результатов можно получить из исходного числа 113 в ходе исполнения программы, содержащей ровно 17 команд?

# ПОПРОБОВАТЬ ИСПРАВИТЬ
# from functools import *
#
# @lru_cache(None)
# def f(number, start_count, last_count, result_count):
#     result_count += 1
#     if start_count > last_count:
#         return 0
#     elif start_count == last_count:
#         return result_count
#     else:
#         return f(number - 1, start_count + 1, 17, result_count) + f(number - 2, start_count + 1, 17, result_count) + f(number ** 0.5, start_count + 1, 17, result_count)
#
# print(f(113,0,17, 0))


result = set()
def f(start, step):
    if step == 17:
        result.add(start)
    else:
        if start > 0 and start ** 0.5 == int(start ** 0.5):
            f(int(start ** 0.5), step + 1)
        f(start - 1, step + 1)
        f(start - 2, step + 1)
f(113,0)
print(len(result))