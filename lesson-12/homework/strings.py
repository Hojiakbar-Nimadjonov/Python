import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def check_primes_in_range(start, end, result):
    for num in range(start, end):
        if is_prime(num):
            result.append(num)

def find_primes_multithreaded(start, end, num_threads=4):
    threads = []
    results = [[] for _ in range(num_threads)]
    step = (end - start) // num_threads

    for i in range(num_threads):
        sub_start = start + i * step
        sub_end = start + (i + 1) * step if i < num_threads - 1 else end
        t = threading.Thread(target=check_primes_in_range, args=(sub_start, sub_end, results[i]))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Объединяем результаты всех потоков
    primes = [p for sublist in results for p in sublist]
    primes.sort()
    return primes

# Пример использования:
if __name__ == "__main__":
    start = 1
    end = 100
    primes = find_primes_multithreaded(start, end, num_threads=4)
    print(f"Простые числа от {start} до {end}:")
    print(primes)

import threading
from collections import Counter
import os

def count_words(lines, result):
    word_count = Counter()
    for line in lines:
        words = line.strip().lower().split()
        word_count.update(words)
    result.append(word_count)

def process_file_multithreaded(filename, num_threads=4):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_lines = len(lines)
    step = total_lines // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start = i * step
        end = (i + 1) * step if i < num_threads - 1 else total_lines
        result = []
        t = threading.Thread(target=count_words, args=(lines[start:end], result))
        threads.append((t, result))
        t.start()

    final_count = Counter()
    for t, result in threads:
        t.join()
        if result:
            final_count.update(result[0])

    return final_count

# Пример использования:
if __name__ == "__main__":
    # Предварительно создайте test.txt с большим текстом
    filename = 'test.txt'
    if os.path.exists(filename):
        word_summary = process_file_multithreaded(filename, num_threads=4)
        print("Слово — количество:")
        for word, count in word_summary.most_common(10):
            print(f"{word}: {count}")
    else:
        print(f"Файл {filename} не найден.")
