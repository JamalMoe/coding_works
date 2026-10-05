def celsius_to_fahrenheit (c) :
    return (c * 9/5) + 32

def fahrenheit_to_celsius (f) :
    return (f - 32) * 5/9

print("1. celsius to fahrenheit")
print("2.fahrenheit to celsuis")
choice = input("choose an option (1 or 2): ")

value = float(input("enter the Temperature: "))

if choice == "1":
    print(f"{value}c = {celsius_to_fahrenheit(value) :.1f}f")
elif choice== "2":
    print(f"{value}f = {fahrenheit_to_celsius(value) :.1f}c")

else:
    print("invalid choice")