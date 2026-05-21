"""
================================
PYTHON LIST COMPREHENSION – NOTES
Topic: Creating lists using one line
================================
"""

# ==================== BASIC EXAMPLES ====================

# Squares of numbers from 1 to 10
# Syntax: [expression for item in iterable]
squares = [number ** 2 for number in range(1, 11)]
print("Squares from 1 to 10:", squares)

# Squares of odd numbers only
# Using step in range to get odd numbers (1, 3, 5, 7, 9)
odd_squares = [number ** 2 for number in range(1, 11, 2)]
print("Squares of odd numbers:", odd_squares)

# ==================== CONDITIONAL COMPREHENSIONS ====================

# Even numbers from 1 to 20
# Syntax: [expression for item in iterable if condition]
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print("Even numbers 1-20:", even_numbers)

# Numbers divisible by 3 or 5
divisible = [num for num in range(1, 31) if num % 3 == 0 or num % 5 == 0]
print("Divisible by 3 or 5:", divisible)

# ==================== IF-ELSE COMPREHENSIONS ====================

# Categorize numbers as "Even" or "Odd"
# Syntax: [value_if_true if condition else value_if_false for item in iterable]
number_types = ["Even" if num % 2 == 0 else "Odd" for num in range(1, 11)]
print("Number types:", number_types)

# Grade letters from scores
scores = [85, 92, 78, 65, 99, 45]
grades = ['A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F' for score in scores]
print("Grades:", list(zip(scores, grades)))

# ==================== NESTED COMPREHENSIONS ====================

# Flatten a 2D matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened matrix:", flattened)

# All possible combinations of two lists
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
combinations = [f"{color} {size}" for color in colors for size in sizes]
print("Color-size combinations:", combinations)

# ==================== STRING COMPREHENSIONS ====================

# Extract vowels from a string
text = "Hello World"
vowels = [char for char in text if char.lower() in 'aeiou']
print("Vowels in text:", vowels)

# Word lengths in a sentence
sentence = "Python is awesome programming language"
word_lengths = [len(word) for word in sentence.split()]
print("Word lengths:", word_lengths)

# ==================== OPTIMIZATION WITH PERFECT SQUARE FUNCTION ====================

# Import the optimized perfect square function
import math

def is_perfect_square_optimized(n):
    """Optimized perfect square check using math.isqrt"""
    if n < 0:
        return False
    root = math.isqrt(n)
    return root * root == n

# Generate perfect squares using list comprehension with optimization
# Instead of generating all squares then filtering, we can be more efficient
perfect_squares = [num for num in range(1, 101) if is_perfect_square_optimized(num)]
print("Perfect squares 1-100:", perfect_squares)

# Alternative: Generate squares directly (more efficient for this specific case)
direct_squares = [i*i for i in range(1, 11)]  # 1^2 to 10^2
print("Direct squares generation:", direct_squares)

# ==================== ADVANCED EXAMPLES ====================

# Prime numbers using Sieve of Eratosthenes concept
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(2, 50) if is_prime(num)]
print("Prime numbers 2-49:", primes)

# Fibonacci numbers up to 100
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(2, 11) if fibonacci[-1] + fibonacci[-2] <= 100]
print("Fibonacci sequence:", fibonacci)

# ==================== EXERCISES ====================

"""
EXERCISE 1: Create a list of cubes of numbers from 1 to 5
Expected: [1, 8, 27, 64, 125]
"""

# Your solution:
cubes = [num ** 3 for num in range(1, 6)]
print("Cubes 1-5:", cubes)

"""
EXERCISE 2: Filter out negative numbers and double the positive ones
Given: [-5, 3, -2, 7, 0, 4]
Expected: [6, 14, 8]
"""

numbers = [-5, 3, -2, 7, 0, 4]
# Your solution:
positive_doubled = [num * 2 for num in numbers if num > 0]
print("Positive numbers doubled:", positive_doubled)

"""
EXERCISE 3: Create a list of palindrome numbers from 1-100
A palindrome reads the same forwards and backwards
Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
"""

# Your solution:
palindromes = [num for num in range(1, 101) if str(num) == str(num)[::-1]]
print("Palindromes 1-100:", palindromes)

"""
EXERCISE 4: Create a list of factorial numbers up to 10!
Expected: [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
"""

# Your solution:
factorials = []
[factorials.append(factorials[-1] * i if factorials else 1) for i in range(1, 11)]
print("Factorials 1-10:", factorials)

"""
EXERCISE 5: Extract all numbers from a mixed string
Given: "abc123def45gh6"
Expected: [1, 2, 3, 4, 5, 6]
"""

mixed_string = "abc123def45gh6"
# Your solution:
extracted_numbers = [int(char) for char in mixed_string if char.isdigit()]
print("Extracted numbers:", extracted_numbers)

print("\n" + "="*50)
print("List Comprehension Examples Complete!")
print("="*50)
