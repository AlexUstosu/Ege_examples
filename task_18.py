'''Решение задачи с помощью файла csv'''
# open file
data_input = []
for line in open('18-0.csv','r+'):
    row = list(map(int, line.split(';')))
    data_input.append(row)

#write input data to console
for i in range(len(data_input)):
    for j in range(len(data_input[i])):
        print(data_input[i][j], end=' ')
    print()

#NxM взять разщмерность
N = len(data_input)             #строки
M = len(data_input[0])          #столбцы

#cxreate new matrix and fill null
data_output = [[0] * M for i in range(N)]

#fill lasty element
data_output[N-1][M-1] = data_input[N-1][M-1]

#fill last row
for column in range(M - 2, -1, -1):
    if data_output[N-1][column] % 3 == 0:
        data_output[N-1][column] = data_output[N-1][column + 1] + data_input[N-1][column]

#fill last column
for row in range(N - 2, -1, -1):
    data_output[row][M -1] = data_output[row + 1][M - 1] + data_input[row][M - 1]

#fill all elements
for row in range(N - 2, -1, -1):
    for column in range(M - 2, -1, -1):
        data_output[row][column] = data_input[row][column] + min(data_output[row+1][column], data_output[row][column+1])

#write result in console
print()

for i in range(len(data_output)):
    for j in range(len(data_output[i])):
        print(data_output[i][j], end=' ')
    print()

#write min/max
print(data_output[0][0])

'''Решение задачи на последовательность'''

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