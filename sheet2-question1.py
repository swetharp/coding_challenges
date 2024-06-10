num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
if num1 > num2 :
    print(f"{num1} is greater than {num2}")
elif num2 == num1:
    print(f"both num1 and num2 are equal")
else:
    print(f"{num2} is greater than {num1}")