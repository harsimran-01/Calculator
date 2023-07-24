while True:

    print("******CALCULATOR*******")

    Num1 = int(input("Please Enter Number 1: "))
    Num2 = int(input("Please Enter Number 2: "))

    operation = input("Please Enter an Operator with which you want to continue. : ")

    if operation == "+":
        print(f"The sum of {Num1} and {Num2} is {Num1 + Num2}.")
    elif operation == "-":
        print(f"The subtraction of {Num1} and {Num2} is {Num1 - Num2}.") 
    elif operation == "*":
        print(f"The product of {Num1} and {Num2} is {Num1 * Num2}.")
    elif operation == "/":
        print(f"The division of {Num1} and {Num2} is {Num1 / Num2}.")       
    elif operation == "**":
        print(f"The square of {Num1} and {Num2} is {Num1 ** Num2}.") 
    elif operation == "//":
        print(f"The Floor Division of {Num1} and {Num2} is {Num1 // Num2}.") 
    elif operation == "%":
        print(f"The Remainder of {Num1} and {Num2} is {Num1 % Num2}.")
    else:
        pass

    play_again = input("Do you want to continue, type (yes or no) : ")
    if play_again.lower() == "no":
        print("Thanks !! The calculator is closed.")
        break
