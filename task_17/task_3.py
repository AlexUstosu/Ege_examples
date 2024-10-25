#233)	В файле 17-1.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000
# до 10 000 включительно. Определите количество троек, в которых хотя бы
# один из трёх элементов меньше, чем среднее арифметическое всех чисел в
# файле, и десятичная запись хотя бы двух из трёх элементов содержит цифру
# 2. В ответе запишите два числа: сначала количество найденных троек,
# а затем – максимальную сумму элементов таких троек. В данной задаче под
# тройкой подразумевается три идущих подряд элемента последовательности.

#2351 17195


# new_list=[]
# pairs=[]
# with open('17-1.txt','r') as file:
#     for line in file:
#         new_list.append(int(line))
# print(new_list)
#
# average = (sum(new_list)/len(new_list))
# print(average)
#
# for i in range(len(new_list)-2):
#     sum = 0
#     k=0
#     x_1 = new_list[i]
#     x_2 = new_list[i + 1]
#     x_3 = new_list[i + 2]
#
#     if x_1 < average or x_2 < average or x_3 < average:
#         k += 1
#
#     sum = x_1 + x_2 + x_3
#     x_1 =  str(x_1)
#     x_2 =  str(x_2)
#     x_3 =  str(x_3)
#
#     count_1 = x_1.count('2')
#     count_2 = x_2.count('2')
#     count_3 = x_3.count('2')
#     if ((count_1 + count_2) >= 2 and count_1 != 0 and count_2 != 0) or \
#        ((count_1 + count_3) >= 2 and count_1 != 0 and count_3 != 0) or \
#        ((count_2 + count_3) >= 2 and count_2 != 0 and count_3 != 0):
#         k += 1
#     if k == 2:
#         pairs.append(sum)
# print(f"Count: {len(pairs)}")
# print(f"MaxSum: {max(pairs)}")

'''
235)	В файле 17-1.txt содержится последовательность целых чисел. 
Элементы последовательности могут принимать целые значения от –10 000 до 
10 000 включительно. Определите количество троек, в которых хотя бы два из 
трёх элементов больше, чем среднее арифметическое всех чисел в файле. 
В ответе запишите два числа: сначала количество найденных троек, 
а затем – максимальную сумму элементов таких троек. В данной задаче 
под тройкой подразумевается три идущих подряд элемента последовательности.
'''



# 12 4 5 6 7 0
# 12 4 5
# 4 5 6
# 5 6 7
# 6 7 0

# 12 22 0
# 222222 0 13

#5020 28715

# new_list = []
# pairs = []
# with open ('17-1.txt', 'r') as file:
#     for line in file:
#         new_list.append(int (line))
# print (new_list)
#
#
# average = (sum(new_list) / len(new_list))
# print (average)
#
# for i in range (len(new_list) - 2):
#     x_1 = new_list[i]
#     x_2 = new_list[i + 1]
#     x_3 = new_list[i + 2]
#
#     if (x_1  > average and x_2  > average) or (x_1  > average and x_3  > average) or (x_2  > average and x_3  > average):
#         pairs.append(x_1 + x_2 +x_3)
#
# print(f"Count: {len(pairs)}")
# print(f"MaxSum: {max(pairs)}")


#317)	(М. Шагитов) В файле 17-316.txt содержится последовательность целых чисел.
# Элементы последовательности – четырёхзначные натуральные числа.
# Назовём два различных четырёхзначных числа неудачной парой,
# если они различаются только цифрами в двух разрядах.
# Найдите все тройки элементов последовательности,
# в которых есть хотя бы одна неудачная пара,
# а сумма всех чисел тройки больше минимальной
# суммы трёх различных элементов последовательности.
# В ответе запишите количество найденных троек,
# затем максимальную из сумм элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

# def isLuckyPair(num1, num2):
#     str_num1 = str(num1)
#     str_num2 = str(num2)
#
#     if len(str_num1) == 4 and len(str_num2) == 4:
#         diff_rank = sum(1 for a, b in zip(str_num1, str_num2) if a != b)
#         if diff_rank == 2:
#             return True
#     return False
#
# new_list = []
# troyki_list = []
# with open('17-316.txt', 'r') as file:
#     for line in file:
#         new_list.append(int(line))
# print(new_list)
#
# sort_list = sorted(new_list)
# print(sort_list)
# min_sum = sort_list[0] + sort_list[1] + sort_list[2]
# print(min_sum)
#
# for i in range(len(new_list) - 2):
#     flag = 0
#     summ = 0
#     x_1 = new_list[i]
#     x_2 = new_list[i+1]
#     x_3 = new_list[i+2]
#
#     if isLuckyPair(x_1, x_2) or isLuckyPair(x_1, x_3) or isLuckyPair(x_3, x_2):
#         flag += 1
#     summ = x_1 + x_2 + x_3
#     if summ > min_sum:
#         flag += 1
#
#     if flag == 2:
#         troyki_list.append(summ)
#
#
# print(f"Count: {len(troyki_list)}")
# print(f"MaxSum: {max(troyki_list)}")


# 318)	(М. Шагитов) В файле 17-316.txt содержится последовательность целых чисел.
# Элементы последовательности – четырёхзначные натуральные числа.
# Назовём два различных четырёхзначных числа хорошей парой,
# если они имеют ровно одну общую цифру в каком-то из разрядов.
# Найдите все тройки элементов последовательности,
# в которых есть хотя бы одна хорошая пара,
# а сумма всех чисел тройки меньше максимальной
# суммы двух различных элементов последовательности.
# В ответе запишите количество найденных троек, затем минимальную
# из сумм элементов таких троек. В данной задаче под тройкой подразумевается
# три идущих подряд элемента последовательности.


def isLuckyPair(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)

    if len(str_num1) == 4 and len(str_num2) == 4:
        diff_rank = sum(1 for a, b in zip(str_num1, str_num2) if a == b)
        if diff_rank == 1:
            return True
    return False

new_list = []
troyki_list = []
with open('17-316.txt', 'r') as file:
    for line in file:
        new_list.append(int(line))
print(new_list)

sort_list = sorted(new_list, reverse=True)
print(sort_list)
max_sum = sort_list[0] + sort_list[1] + sort_list[2]
print(max_sum)


for i in range(len(new_list) - 2):
    flag = 0
    summ = 0
    x_1 = new_list[i]
    x_2 = new_list[i+1]
    x_3 = new_list[i+2]

    if isLuckyPair(x_1, x_2) or isLuckyPair(x_1, x_3) or isLuckyPair(x_3, x_2):
        flag += 1
    summ = x_1 + x_2 + x_3
    if summ < max_sum:
        flag += 1

    if flag == 2:
        troyki_list.append(summ)


print(f"Count: {len(troyki_list)}")
print(f"MaxSum: {max(troyki_list)}")



#371)	В файле 17-370.txt содержится последовательность целых чисел, по модулю
# не превышающих 20000.  Определите количество пар элементов последовательности, в которых
#– только одно число четырёхзначное;
#– сумма квадратов элементов пары делится нацело на максимальное трёхзначное
# число в последовательности, сумма цифр которого оканчивается на 3.
#В ответе запишите сначала количество найденных пар, затем максимальную
# из сумм квадратов элементов таких пар. Под парой элементов подразумеваются
# два соседних элемента последовательности.

tr_list = [i for i in new_list if len(str(i)) == 3]
tr_end_list = [i for i in tr_list if i % 10 + i == ]

result = (x_1**2 + x_2**2) //



