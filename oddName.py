"""
Corey Jamieson
"""
def main():
    try:
        get_name()
    except ValueError:
        print("Please enter valid name")


def get_name():
    name = str(input("Please enter name"))
    while name == ():
        name = str(input("Please enter valid name"))
    print(name[0:2])


main()
