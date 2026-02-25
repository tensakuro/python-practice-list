"""
================================
PYTHON LIST COMPREHENSION – NOTES
Topic: Creating lists using one line
================================
"""

# Squares of numbers from 1 to 10
squares = [number ** 2 for number in range(1, 11)]
print("Squares from 1 to 10:", squares)

# Squares of odd numbers
odd_squares = [number ** 2 for number in range(1, 11, 2)]
print("Squares of odd numbers:", odd_squares)
