Number_One = input("Enter first number: ")
Number_Two = input("Enter second number: ")
Calculation_Type = input("Choose between:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division:\n")


    # Addition
if Calculation_Type == "1":
    print(float (Number_One) + float (Number_Two))

    # Subtraction
elif Calculation_Type == "2":
    print(float (Number_One) - float (Number_Two))

    # Multiplication
elif Calculation_Type == "3":
    print(float (Number_One) * float (Number_Two))

    # Division
elif Calculation_Type == "4":
    print(float (Number_One) / float (Number_Two))

else:
    print("Please choose a number between 1 to 4.")