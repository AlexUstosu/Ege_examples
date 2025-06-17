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


