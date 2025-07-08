a = float(input("enter a number a"))
b = float(input("enter a number b"))
minus =input("minus(-) Y/N")
plus =input("plus(+) Y/N")
multiple =input("multiple(*) Y/N")
devide =input("devide(/) Y/N")
power =input("minus(**) Y/N")

if minus == "Y" or minus == "y":
    print( a - b)
elif minus == "N" or minus == "n":
    print("NULL")
else:
    print("enter a nuber")

if plus == "Y" or plus == "y":
    print( a + b)
elif plus == "N" or plus == "n":
    print("NULL")
else:
    print("enter a nuber")

if multiple == "Y" or multiple == "y":
    print( a * b)
elif multiple == "N" or multiple == "n":
    print("NULL")
else:
    print("enter a nuber")

if devide == "Y" or devide == "y":
    if b != 0 or a != 0:
        print( a / b)
    else:
        print("cannot divide by zero")
elif devide == "N" or devide == "n":
    print("NULL")
else:
    print("enter a nuber")

if power == "Y" or power == "y":
    print( a ** b)
elif power == "N" or power == "n":
    print("NULL")
else:
    print("enter a nuber")