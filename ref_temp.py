"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def celsius_calc():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def fahrenheit_calc():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            result = celsius_calc()
            print("Result: {:.2f} F".format(result))
        elif choice == "F":
            result = fahrenheit_calc()
            print("Result: {:.2f} C".format(result))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()
