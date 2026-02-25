"""
================================
PYTHON BASICS – CLEAN NOTES
Topic: Core Python fundamentals
================================
"""

# --------------------------------
# 1. VARIABLES & USER INPUT
# --------------------------------

is_fees_paid = True
is_available = False
price = 68000

mobile_name = input("Enter mobile name: ")
budget = int(input("Enter your budget: "))
color = input("Enter your desired color: ")

BUDGET_STARTS_FROM = 50000   # constant-style naming

# --------------------------------
# 2. LIST (Store multiple values)
# --------------------------------

mobiles = ["iphone", "samsung", "oneplus", "nokia", "redmi"]
print("Available mobiles:", mobiles)

# --------------------------------
# 3. CONDITIONAL STATEMENTS
# --------------------------------

if budget >= BUDGET_STARTS_FROM:
    print(f"You can buy the {color} {mobile_name} mobile")
else:
    print(
        f"You cannot buy the {color} {mobile_name} mobile "
        f"because your budget is less than {BUDGET_STARTS_FROM}"
    )

# --------------------------------
# 4. STRING METHODS
# --------------------------------

name = "Ada Lovelace"
print(name.upper())
print(name.lower())
print(name.title())

# --------------------------------
# 5. f-STRINGS (String formatting)
# --------------------------------

print(f"Hello, {name.title()}!")

# --------------------------------
# 6. WHITESPACE HANDLING
# --------------------------------

favourite_language = "  python  hello  "
print("Original:", favourite_language)
print("Stripped:", favourite_language.strip())

# --------------------------------
# 7. NUMBERS & READABILITY
# --------------------------------

universe_age = 14_000_059   # underscores improve readability
print("Universe age:", universe_age)

# --------------------------------
# 8. MULTIPLE ASSIGNMENT
# --------------------------------

x, y, z = 5, 10, 15
print("Sum:", x + y + z)

# --------------------------------
# 9. PROFIT / LOSS PROGRAM
# --------------------------------

revenue = int(input("Enter the revenue: "))
expenses = int(input("Enter the expenses: "))

profit_or_loss = revenue - expenses

if profit_or_loss > 0:
    print(f"The company is in profit. Profit = {profit_or_loss}")
elif profit_or_loss < 0:
    print(f"The company is in loss. Loss = {-profit_or_loss}")
else:
    print("No Profit, No Loss")
