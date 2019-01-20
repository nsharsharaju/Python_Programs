import math

user_input = int(input("Enter the number that you want check prime or not: "))

i = 2
flag = 0
if user_input<=0:
    print("The number you entered is Negative or Zero")
elif user_input==1:
    print("The number you entered is neither prime nor non-prime")
elif user_input==2:
    print("The number you entered is prime",user_input)
else:
    while(i<int(math.sqrt(user_input))):
        if user_input%i==0:
            print("The number you entered is not prime",user_input)
            flag = 1
            break
        i += 1
    if flag==0:
        print("The number you entered is prime")
