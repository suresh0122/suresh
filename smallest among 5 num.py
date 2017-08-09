

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
num5 = int(input("Enter fifth number: "))
if (num1 > num2) & (num1 > num3) & (num1 > num4) & (num1 > num5):
    print("num1 is largest")
elif (num2 > num1) &(num2 > num3) & (num2 > num4) & (num2 > num5):
    print("num2 is largest")
elif (num3 > num1) &(num3 > num2) & (num3 > num4) & (num4 > num5):
    print("num3 is largest")
elif (num4 > num1) &(num4 > num2) & (num4 > num3) & (num4 > num5):
    print("num4 is largest")
else:
    print("num5 is largest")

