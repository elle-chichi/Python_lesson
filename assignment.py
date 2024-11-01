# 1. Write a function reverse_string(s) that takes a string s and returns the reversed string
def reverse_string(s):
    return s[::-1]

# Example usage:
result = reverse_string("melon")
print(result)

# 2. Create a function is_palindrome(word) that returns True if a given word is a palindrome (reads the same backward) and False otherwise.
def is_palindrome(word):
    # Normalize the word by converting it to lowercase
    normalized_word = word.lower()
    # Check if the word is the same when reversed
    return normalized_word == normalized_word[::-1]

# Example usage:
print(is_palindrome("madam"))
print(is_palindrome("muffum"))
print(is_palindrome("yellow"))

# 3. Write a function fibonacci(n) that generates a list containing the first n numbers in the Fibonacci sequence.
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_fib)

    return fib_sequence
print(fibonacci(12))