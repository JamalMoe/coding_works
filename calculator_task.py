def calculate (nums1, nums2, operator):
    if operator == "+":
        return nums1 + nums2
    elif operator == "-":
        return nums1 - nums2
    elif operator == "/":
        return nums1 / nums2
    elif operator == "*":
        return nums1 * nums2
    else:
        return ("wrong operator, please choose one of these: +, -, / or *")

a = float(input("enter first number: "))
op = input("enter operator (+, -, *, /): ")
b = float(input("enter second number: "))

print("result: ", calculate(a,b,op))