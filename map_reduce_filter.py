from functools import reduce

# Пример map()
numbers = [1, 2, 3, 4,-10,-15]
squared = list(map(lambda x: x**2, numbers))
#print(squared) # [1, 4, 9, 16]
# Пример filter()
even_numbers= list(filter(lambda x: x % 2 == 0 and x > 0, numbers))
print(even_numbers) # [2, 4]
# Пример reduce()

product = reduce(lambda x, y: x if(x > y) else y, numbers)
#print(product)