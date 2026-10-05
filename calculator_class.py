def calculate (nums1, nums2, operator):
    if operator == "+":
        return nums1 + nums2
    elif operator == "-":
        return nums1 - nums2
    elif operator == "/":
        return nums1/nums2
    elif operator == "*":
        return nums1 * nums2
    else:
        return ("Wrong operator, please choose one of these: +, -, / or *")

a = float(input("Enter the first number: "))
op = input("Please choose one of these: +, -, / or *: ")
b = float(input("Enter the second number: "))

print("Result: ", calculate(a,b,op))