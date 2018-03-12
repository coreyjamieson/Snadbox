"""
Corey Jamieson
"""

try:
    name = str(input("Please enter name"))
    while name == ():
        name = str(input("Please enter valid name"))
    print(name[0:2])
except ValueError:
    print("Please enter valid name")