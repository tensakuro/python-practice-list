"""
================================
PYTHON FOR LOOPS – CLEAN NOTES
Topic: Looping with lists and range()
================================
"""

# Looping through a list
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]

for cycle in motorcycles:
    print(cycle.title())
    print(f"I would like to own a {cycle.title()} motorcycle.\n")

print("I really love motorcycles!")

# Using range()
for value in range(1, 6):
    print(value)

# Converting range to list
numbers = list(range(1, 6))
print("Numbers:", numbers)

# range with step value
even_numbers = list(range(2, 11, 2))
print("Even numbers:", even_numbers)
