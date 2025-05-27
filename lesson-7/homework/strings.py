# Example: Square every number in a list
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16, 25]
# Example: Filter even numbers
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4, 6]
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Examples
print(is_prime(4))  # False
print(is_prime(7))  # True
def digit_sum(k):
    return sum(map(int, str(k)))

# Examples
print(digit_sum(24))   # 6  (2 + 4)
print(digit_sum(502))  # 7  (5 + 0 + 2)
def powers_of_two(N):
    result = []
    i = 1
    while (2 ** i) <= N:
        result.append(2 ** i)
        i += 1
    return result

# Example
print(powers_of_two(10))  # [2, 4, 8]
def powers_of_two_v2(N):
    return list(filter(lambda x: x <= N, map(lambda i: 2**i, range(1, N))))

# Example
print(powers_of_two_v2(10))  # [2, 4, 8]
