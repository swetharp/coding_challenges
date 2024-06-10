#calculator
choice = input("Enter your choice of option as 1 for Add, 2 for Subtract, 3 for Multiply and 4 for Divide: ")
num1 = int(input("enter num1: "))
num2 = int(input("enter num2: "))
if choice == "1":
    print(f"Addition of {num1} and {num2} is ",num1+num2)
elif choice == "2":
    print(f"Subtraction of {num2} from {num1} is ",num1-num2)
elif choice == "3":
    print(f"Multiplication of {num1} and {num2} is ",num1*num2)
elif choice == "4":
    print(f"Division of {num1} from {num2} is ",num1/num2)