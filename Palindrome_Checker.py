text = input("enter a word or phrase: ")

cleaned = text

if cleaned == cleaned[::-1]:
    print(f'"{text}" is a palindrome')

else:
    print(f'"{text}" is not a palindrome')  