x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x==y:
    if y!=0:
        print("x/y",x/y)
elif x<y:
    print("x is smaller")
else:
    print("y is smaller")