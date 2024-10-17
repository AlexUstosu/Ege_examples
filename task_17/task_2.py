#232)	В файле 17-1.txt содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от –10 000
# до 10 000 включительно. Определите количество троек, в которых хотя
# бы один из трёх элементов меньше, чем среднее арифметическое всех
# чисел в файле, и десятичная запись хотя бы одного из трёх элементов
# содержит цифру 8. В ответе запишите два числа: сначала количество
# найденных троек, а затем – максимальную сумму элементов таких троек.
# В данной задаче под тройкой подразумевается три идущих подряд элемента
# последовательности.

# 1 15 89 12 3
# 1 15 89 -
# 15 89 12 -
# 89 12 3 -

list_number = []
list_pairs = []
file = open('17-1.txt','r')
for line in file:
    list_number.append(int(line))

print(list_number)
average = sum(list_number) / len(list_number)
print(average)

for i in range(len(list_number) - 2):
    number_str = ''
    right_rools = 0
    n_1 =   list_number[i]
    n_2 =   list_number[i + 1]
    n_3 =   list_number[i + 2]

    if n_1 < average or n_2 < average or n_3 < average:
        right_rools += 1

    number_str = str(n_1) + str(n_2) + str(n_3)
    count_3 = number_str.count('8')

    if count_3 > 0:
        right_rools += 1

    if right_rools == 2:
        list_pairs.append(n_1 + n_2 + n_3)

print(f"Count: {len(list_pairs)}")
print(f"Summ max: {max(list_pairs)}")