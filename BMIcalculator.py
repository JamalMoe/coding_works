def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def classify(bmi):
    if bmi < 18.5:
        return "underweight"

    elif bmi < 25:
        return "normal weight"

    elif bmi < 30:
        return "overweight"

    else:
        return "obese"


weight = float(input("enter your weight in kg: "))
height = float(input(" enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print(f"your bmi is {bmi:.1f} ({classify(bmi) })")