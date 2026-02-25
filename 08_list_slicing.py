"""
================================
PYTHON LIST SLICING – CLEAN NOTES
Topic: Accessing parts of a list
================================
"""

players = ["charles", "martina", "michael", "florence", "eli"]

# Slicing examples
print("First three players:", players[:3])
print("Middle players:", players[1:4])
print("From index 2 to end:", players[2:])
print("Last three players:", players[-3:])

# Looping over slices
print("\nTop 3 players:")
for player in players[:3]:
    print(player.title())

print("\nTop 4 players:")
for player in players[:4]:
    print(player.title())

print("\nLast 3 players:")
for player in players[-3:]:
    print(player.title())
