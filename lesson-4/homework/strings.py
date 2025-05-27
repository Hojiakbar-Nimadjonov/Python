# 1. Сортировка словаря по значению
data = {'a': 3, 'b': 1, 'c': 2}
# По возрастанию
sorted_asc = dict(sorted(data.items(), key=lambda item: item[1]))
# По убыванию
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("По возрастанию:", sorted_asc)
print("По убыванию:", sorted_desc)

# 2. Добавить ключ в словарь
d = {0: 10, 1: 20}
d[2] = 30
print(d)

# 3. Объединение нескольких словарей
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
merged_dict = {**dic1, **dic2, **dic3}
print(merged_dict)

# 4. Создание словаря с квадратами от 1 до n
n = 5
squares = {x: x**2 for x in range(1, n+1)}
print(squares)

# 5. Словарь квадратов от 1 до 15
square_dict = {x: x**2 for x in range(1, 16)}
print(square_dict)
# 1. Создать набор
my_set = set([1, 2, 3, 4])
print("Созданный набор:", my_set)

# 2. Итерация по набору
for item in my_set:
    print(item)

# 3. Добавить участника(ов) в набор
my_set.add(5)
my_set.update([6, 7])  # Добавление нескольких элементов
print("После добавления:", my_set)

# 4. Удалить элемент(ы) из набора
my_set.discard(3)  # Без ошибки, если элемента нет
my_set.remove(2)   # Ошибка, если элемента нет
print("После удаления:", my_set)

# 5. Удалить элемент, если он присутствует
element = 6
if element in my_set:
    my_set.remove(element)
print("После условного удаления:", my_set)
