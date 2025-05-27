# 1. Создание и доступ к элементам списка
fruits = ['яблоко', 'банан', 'киви', 'апельсин', 'груша']
print(fruits[2])  # третий фрукт

# 2. Объединить два списка
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)

# 3. Извлечение элементов из списка
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print(new_list)

# 4. Преобразовать список в кортеж
movies = ['Матрица', 'Начало', 'Интерстеллар', 'Титаник', 'Аватар']
movies_tuple = tuple(movies)
print(movies_tuple)

# 5. Проверка элемента в списке
cities = ['Лондон', 'Берлин', 'Париж', 'Мадрид']
print('Париж' in cities)

# 6. Дублирование списка без использования циклов
nums = [1, 2, 3]
duplicated = nums * 2
print(duplicated)

# 7. Поменять местами первый и последний элементы списка
values = [9, 8, 7, 6, 5]
values[0], values[-1] = values[-1], values[0]
print(values)

# 8. Разрежьте кортеж
numbers_tuple = tuple(range(1, 11))
print(numbers_tuple[3:8])  # с индексами от 3 до 7 включительно

# 9. Подсчет вхождений в список
colors = ['синий', 'красный', 'зелёный', 'синий', 'жёлтый', 'синий']
count_blue = colors.count('синий')
print(count_blue)

# 10. Найдите индекс элемента в кортеже
animals = ('тигр', 'слон', 'лев', 'жираф')
index_lion = animals.index('лев')
print(index_lion)

# 11. Объединить два кортежа
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# 12. Найдите длину списка и кортежа
lst = [10, 20, 30]
tup = (100, 200, 300, 400)
print(len(lst), len(tup))

# 13. Преобразовать кортеж в список
numbers_t = (7, 8, 9, 10, 11)
numbers_l = list(numbers_t)
print(numbers_l)

# 14. Найти максимум и минимум в кортеже
values_t = (25, 10, 5, 100, 50)
print(max(values_t), min(values_t))

# 15. Перевернуть кортеж
words = ('привет', 'как', 'дела', 'у', 'тебя')
reversed_words = words[::-1]
print(reversed_words)
