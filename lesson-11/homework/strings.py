python -m venv myenv

myenv\Scripts\activate
project/
│
├── math_operations.py
├── string_utils.py
│
├── geometry/
│   ├── __init__.py
│   └── circle.py
│
└── file_operations/
    ├── __init__.py
    ├── file_reader.py
    └── file_writer.py
# math_operations.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
# string_utils.py

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOUаеёиоуыэюяАЕЁИОУЫЭЮЯ"
    return sum(1 for char in s if char in vowels)
# geometry/__init__.py
# Можно оставить пустым или использовать для импорта

from .circle import calculate_area, calculate_circumference
# geometry/circle.py

import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
# file_operations/__init__.py
# Можно оставить пустым или использовать для объединения

from .file_reader import read_file
from .file_writer import write_file
# file_operations/file_reader.py

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Файл не найден."
# file_operations/file_writer.py

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
from math_operations import add, divide
from string_utils import reverse_string
from geometry import calculate_area
from file_operations import read_file, write_file

print(add(3, 4))  # 7
print(divide(10, 2))  # 5.0
print(reverse_string("Python"))  # nohtyP
print(calculate_area(5))  # Площадь круга

write_file("example.txt", "Привет, мир!")
print(read_file("example.txt"))
