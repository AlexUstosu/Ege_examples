left = 1 * 7 ** 2 + 0 + 1
right = left - 1
for i in range(3,100):
    chislo = 1 * i ** 2 + 2 * i + 1
    if chislo == right:
        x = i
        break

x_3 = ''
while x > 0:
    x_3 += str(x % 3)
    x //= 3

x_3 = x_3[::-1]
print(x_3)


