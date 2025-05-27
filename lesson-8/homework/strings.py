#ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
  
  #ValueError
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not a valid integer.")

#FileNotFoundError
try:
    with open("nonexistent_file.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
  
#TypeError
try:
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    result = a + b  # Wrong if a and b are strings
    print(int(result))
except TypeError:
    print("Invalid type for operation.")

#PermissionError
    with open("/root/secret.txt") as f:
        print(f.read())
except PermissionError:
    print("You don't have permission to access this file.")

#IndexError
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("Index out of range.")
  
#KeyboardInterrupt
try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")
  
#ArithmeticError
try:
    x = 10 / 0
except ArithmeticError:
    print("Arithmetic error occurred.")
  
#UnicodeDecodeError
try:
    with open("file.txt", encoding="ascii") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Encoding error reading the file.")
  
#AttributeError
try:
    x = 10
    x.append(5)  # int has no 'append'
except AttributeError:
    print("Attribute does not exist for object.")

with open("example.txt", "r") as f:
    print(f.read())


n = 3
with open("example.txt", "r") as f:
    for i in range(n):
        print(f.readline().strip())


with open("example.txt", "a") as f:
    f.write("New line added.\n")
with open("example.txt") as f:
    print(f.read())


from collections import deque
n = 3
with open("example.txt") as f:
    last_lines = deque(f, n)
print("".join(last_lines))



with open("example.txt") as f:
    lines = f.readlines()



with open("example.txt") as f:
    content = f.read()


with open("example.txt") as f:
    chars = list(f.read())


with open("example.txt") as f:
    words = f.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)


with open("example.txt") as f:
    print("Line count:", len(f.readlines()))


from collections import Counter
with open("example.txt") as f:
    words = f.read().split()
    freq = Counter(words)
    print(freq)


import os
print(os.path.getsize("example.txt"), "bytes")


data = ['one', 'two', 'three']
with open("output.txt", "w") as f:
    for item in data:
        f.write(item + "\n")


with open("example.txt") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())


with open("file1.txt") as f1, open("file2.txt") as f2, open("output.txt", "w") as out:
    for line1, line2 in zip(f1, f2):
        out.write(line1.strip() + " " + line2)


import random
with open("example.txt") as f:
    lines = f.readlines()
    print(random.choice(lines).strip())


f = open("example.txt")
f.close()
print(f.closed)


with open("example.txt") as f:
    lines = [line.strip() for line in f]


with open("example.txt") as f:
    words = f.read().replace(",", " ").split()
    print("Word count:", len(words))


chars = []
for filename in ["file1.txt", "file2.txt"]:
    with open(filename) as f:
        chars.extend(list(f.read()))
print(chars)


import string
for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w") as f:
        f.write(f"This is file {letter}")


import string
n = 5
with open("letters.txt", "w") as f:
    for i in range(0, 26, n):
        f.write("".join(string.ascii_uppercase[i:i+n]) + "\n")



