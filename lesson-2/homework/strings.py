#1. Age Calculator
name = input("Введите ваше имя: ")
year_of_birth = int(input("Введите ваш год рождения: "))
current_year = 2025
age = current_year - year_of_birth
print(f"{name}, вам {age} лет.")

#2. Extract Car Names
txt = 'LMaasleitbtui'
car = txt[::2]  # L, a, s, e, b, u → 'Lasebu'
print(car)  # Возможное название: 'Lambui'

#3. Extract Car Names
txt = 'MsaatmiazD'
car = txt[::2]  # M, a, t, a, z → 'Mataz'
print(car)  # Возможное название: 'Mazda'

#4. Extract Residence Area
txt = "I'am John. I am from London"
city = txt.split("from")[-1].strip()
print("Жилой район:", city)

#5. Reverse String
s = input("Введите строку: ")
print("Обратная строка:", s[::-1])

#6. Count Vowels
s = input("Введите строку: ").lower()
vowels = "aeiouаеёиоуыэюя"
count = sum(1 for char in s if char in vowels)
print("Количество гласных:", count)

#7. Find Maximum Value
nums = list(map(int, input("Введите числа через пробел: ").split()))
print("Максимальное значение:", max(nums))

#8. Check Palindrome
word = input("Введите слово: ").lower()
if word == word[::-1]:
    print("Это палиндром.")
else:
    print("Это не палиндром.")

#9. Extract Email Domain
email = input("Введите email: ")
domain = email.split("@")[-1]
print("Домен:", domain)

#10. Generate Random Password
import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choices(chars, k=12))
print("Случайный пароль:", password)
