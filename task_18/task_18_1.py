# 51)(А. Кабанов) Дана последовательность натуральных чисел. Рассматриваются
# всевозможные пары чисел, порядковые номера которых отличаются не более чем на 5.
# Определите минимальную чётную сумму среди таких пар. Исходные данные записаны в виде
# столбца электронной таблицы в файле 18-k3.xls.
# open file
data_input = []
for line in open('18-k3.csv','r+'):
    data_input.append(int(line))

minimum = 1000000
for i in range(len(data_input) - 6):
    for j in range(i + 1, i + 6):
        summ = data_input[i] + data_input[j]
        if summ % 2 == 0:
            minimum = min(minimum, summ)


print(minimum)