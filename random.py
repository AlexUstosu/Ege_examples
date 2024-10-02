
import random as rnd

# rnd.random()    #0.0
# rnd.randint(4, 500)
# rnd.randrange(8,28,2)
# rnd.choice(['a', 'b', 'c', 'd', 'e', 'f'])
# rnd.shuffle(['a', 'b', 'c', 'd', 'e', 'f'])
#
#
#
# random_list = []
# N = int(input("Введите N: "))
#
# for i in range(N):
#     random_list.append(rnd.randint(-20,20))
#
# #random_list.sort()
#
# min_element = min(random_list)
# max_element = max(random_list)
#
# print("min = ", min_element,'\nmax = ', max_element)
#
# print(random_list)
#
# print('Count of max=', random_list.count(max_element))
# print('Count of min=', random_list.count(min_element))
#
#
# for i in range(random_list.count(max_element)):
#     random_list.remove(max_element)
#
# for i in range(random_list.count(min_element)):
#     random_list.remove(min_element)
#
# print(random_list)
#
#
#
# print('Sred= ',sum(random_list) / len(random_list))

#147)	(А. Кабанов) Рассматривается множество целых чисел, принадлежащих полуинтервалу
# (1220; 11200], которые делятся на 5 и не делятся на 7, 13, 17 и 19. Найдите количество
# таких чисел и разницу между максимальным и минимальным числом


generate_list = [i for i in range(1221,11201)]
clear_list = []
for element in generate_list:
    if element % 5 == 0 and element % 7 != 0 and element % 13 != 0 and element % 17 != 0 \
        and element % 19 != 0:
        clear_list.append(element)


print(len(clear_list))
print(max(clear_list) - min(clear_list))



