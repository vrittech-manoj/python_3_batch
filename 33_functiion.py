# def add():
#     a = int(input("Enter first number"))
#     b = int(input("Enter second number"))
#     print(a+b)

#WAP for calculator without using functio

a = int(input("Enter first number#>>>"))
operator = input("Enter operator#>>>")
b = int(input("Enter second number#>>>"))

def sum():
    sum = a+b
    print("addition of a and b is ",sum)

def subtract():
    subtract = a-b
    print("addition of a and b is ",subtract)

if operator == "+":
    sum()
elif operator == "-":
    subtract()

   


