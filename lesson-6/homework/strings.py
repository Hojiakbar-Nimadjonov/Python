def insert_underscores(txt):
    result = []
    i = 0
    while i < len(txt):
        # добавляем три символа, если остались
        chunk = txt[i:i+3]
        result.append(chunk)
        i += 3
        # проверка необходимости подчеркивания
        if i < len(txt):
            if txt[i-1] not in "aeiouAEIOU" and (i >= len(txt) or txt[i] != "_"):
                result.append("_")
    return ''.join(result)

print(insert_underscores("hello"))          # hel_lo
print(insert_underscores("assalom"))        # ass_alom
print(insert_underscores("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef

n = int(input())
for i in range(n):
    print(i ** 2)

i = 1
while i <= 10:
    print(i)
    i += 1

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=' ')
    print()
num = int(input("Enter number: "))
total = sum(range(1, num+1))
print("Sum is:", total)
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num > 100:
        print(num)
num = 75869
count = len(str(num))
print("Output:", count)
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)
for i in range(-10, 0):
    print(i)
for i in range(5):
    print(i)
print("Done!")
print("Prime numbers between 25 and 50:")
for num in range(25, 51):
    if num > 1:
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                break
        else:
            print(num)
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
num = int(input("Enter number: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f"{num}! = {factorial}")

from collections import Counter

def uncommon_elements(list1, list2):
    c1 = Counter(list1)
    c2 = Counter(list2)
    result = []

    for elem in c1:
        if elem not in c2:
            result.extend([elem] * c1[elem])
    for elem in c2:
        if elem not in c1:
            result.extend([elem] * c2[elem])
    return result

print(uncommon_elements([1, 1, 2], [2, 3, 4]))         # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))         # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
