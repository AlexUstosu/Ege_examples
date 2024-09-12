ex = 49 ** 7 + 7 ** 21 - 7 ** 1
count = 0
while ex:
    if ex % 7 == 6:
        count = count + 1
    ex = ex // 7

print(count)

