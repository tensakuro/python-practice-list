"""
================================
PYTHON LISTS – BASICS
Topic: Creating and accessing lists
================================
"""

bicycles = ["trek", "cycle", "redline", "specialized"]

print("Bicycles:", bicycles)
print("First:", bicycles[0])
print("Last:", bicycles[-1])


cycle=bicycles[:]

print("Cycle:", cycle)

cycle.append("giant")

print("Cycle after append:", cycle)