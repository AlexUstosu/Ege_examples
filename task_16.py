'''
Задача на рекурсивный алгоритм
1. Выход из алгоритма / конечные условия
2. Ограничения / условия
3. Какой шаг
4. Вызов

f(1)
----------------
f(2)
--------------
f(3)
--------------
f(4)
------------------
f(5)
---------------
'''
#______________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________
#Р-05 (И.В. Свиридкин). Алгоритм вычисления функции F(n) задан следующими соотношениями:
# 		F(n) = 2n при n <= 5
# 		F(n) = F(n–2) + 3F(n/2) + n, если n > 5 и  чётно,
# 		F(n) = F(n–1) + F(n–2) + F(n–3), если n > 5 и нечётно.
# Чему равно значение функции F(99) + F(100)?

# from functools import lru_cache
#
# # import sys
# # sys.setrecursionlimit(5000)
#
# @lru_cache(None)
# def F(n):
#     if n <= 5:
#         return 2 * n
#     if n > 5 and n % 2 == 0:
#         return F(n - 2) + 3 * F(n // 2) + n
#     else:
#         return F(n - 1) +  F(n - 2) + F(n - 3)
#
# print(F(99) + F(1000))
#______________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________
#Р-02. Определите, сколько символов * выведет эта процедура при вызове F(22):
# count = 0
#
# def F( n ):
#   global count
#   #print('*')
#   count += 1
#   if n >= 1:
#     #print('*')
#     count += 1
#     F(n-1)
#     F(n-2)
#     F(n-3)
#
#
# F(22)
# print(count)
#______________________________________________________________________________________________________________________
#______________________________________________________________________________________________________________________
# from functools import lru_cache
#
# @lru_cache(None)
# def f(n):
#   if n == 0:
#     return 1
#   if n == 1:
#     return 3
#   if n > 1 and n % 2 == 0:
#     return f(n - 1) - f(n - 2) + 3 * n
#   if n > 1 and n % 2 != 0:
#     return f(n - 2) - f(n - 3) + 2 * n
#
#
# print(f(40))