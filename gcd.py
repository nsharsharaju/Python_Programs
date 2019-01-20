number1 = int(input("Enter the 1st number "))
number2 = int(input("Enter the 2nd number "))
while number1!=number2:
    if number1>number2:
        number1 = number1-number2
    else:
        number2 = number2-number1
print("The GCD of the two number you entered is",number1)