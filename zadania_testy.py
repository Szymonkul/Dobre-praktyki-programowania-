import math
import re


def is_palindrome(text):
    text = text.lower().replace(' ', '')
    return text == text[::-1]


def fibonacci(n):
    if n < 0:
        raise ValueError('n must be greater or equal than 0')
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'ą', 'ę', 'y', 'ó']
    result = 0
    for letter in text.lower():
        if letter in vowels:
            result += 1
    return result


def calculate_discount(price, discount) -> float:
    if price < 0:
        raise ValueError("Price must be non-negative")
    if not (0 <= discount <= 1):
        raise ValueError("Discount must be between 0 and 1")

    return price * (1 - discount)


def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

def word_frequencies(text: str) -> dict:
    result = {}
    words = re.findall(r'\b\w+\b', text.lower())
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

print(word_frequencies("To be or not to be"))
word_frequencies(" ala ma kotadasda kdamk!")


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
