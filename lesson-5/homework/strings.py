def is_leap(year):
    """Определяет, является ли указанный год високосным.

    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): Год для проверки.

    Returns:
    bool: True — високосный, False — обычный.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print(is_leap(2020))  # True
print(is_leap(1900))  # False
print(is_leap(2000))  # True
n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:  # n > 20 и чётное
    print("Not Weird")
a = 2
b = 10

start = a if a % 2 == 0 else a + 1
end = b + 1
even_numbers = list(range(start, end, 2))
print(even_numbers)
a = 2
b = 10

even_numbers = list(range(a + a % 2, b + 1, 2))
print(even_numbers)
