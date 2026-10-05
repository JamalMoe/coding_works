password= input("Enter your password: ")

has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_lower = any(c.islower() for c in password)
long_enough = len(password) >= 8

if has_upper and has_lower and has_digit and long_enough:
    print("Very strong")

elif long_enough and has_digit and (has_upper or has_lower):
    print("Strong")

elif long_enough and (has_digit or has_lower or has_upper):
    print("Medium")

else:
    print("Weak password")