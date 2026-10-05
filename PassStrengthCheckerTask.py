password = input("enter a password to check: ")
has_upper = any(c.isupper()for c in password)
has_lower = any(c.islower() for c in password)
has_digit = any(c.isdigit() for c in password)
long_enough = len(password) >= 12

if has_upper and has_lower and has_digit and long_enough:
    print("very strong password")

elif long_enough and (has_upper or has_lower):
    print("medium password")

elif long_enough and (has_digit or has_lower):
    print("also medium password")

else:
    print("weak password")