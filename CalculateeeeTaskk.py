def calculate (number1, number2, process):
    if process == "+":
        print (number1 + number2)

    elif process == "-":
        print (number1 - number2)

    elif process == "*":
        print(number1 * number2)

    elif process == "/":
        print(number1 / number2)

num1 = float(input("enter the first number"))
num2 = float(input(" enter the second number"))
proc = input(" enter one of these choices: +, -, *, /")

result = calculate(num1,num2,proc)

print(result)