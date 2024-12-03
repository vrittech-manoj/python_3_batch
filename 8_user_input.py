# input("string") -> str 

# age = input("Enter your age?#>>>")
# print("Your age is ",age)

age = input("Enter your age?#>>>")
age = int(age)

if age>0 and age<13: #(True and False = Fasle)
    print("you are child")
elif age>=13 and age<20:
    print("you are teenagers")
elif age<0 or age>200: #(False or True = True)
    print("wrong input")
else:
    print("either you are adult or old")

    