# types of condition 

# 1)if
# 2)if ... else 
# 3)if ...elif ....elif ...else (nested condition )

# age=30
# if age>18:
#     print("you can vote") 
#     print("you can drink") 
#     print("you can ..") 
#     print("you can vote")

# syntax
# if condition_true:
#     statements
    
# age=15
# if age>18:
#     print("you can vote") 
#     print("you can drink") 
#     print("you can ..") 
#     print("you can vote")
# else:
#     print("you can not vote")

# #class work
# age = 6 #take user input
# # WAP to output like {child,adult....old} 
# if isinstance(age,str) and age.isdigit() == False: # if not age.isdigit():
#     print("invalid age")
# elif age>0 and age<13:
#     print("you are child")
# elif age>=13 and age<20:
#     print("you are teenagers")
# else: 
#     print("wrong input")



mark = int(input("Enter mark percentage#>>>"))

if mark<30: #15 <30 ?
    print("Fail")
elif mark>=30 and mark<40: #True and False
    print("third division")




