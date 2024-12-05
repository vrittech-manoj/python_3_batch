# loop types
# 1)while loop 
# 2)for loop 


# is_satyug = True
# i = 0
# while is_satyug:
#     print("Hello NPL!!!")
#     if i==5: #True
#         is_satyug = False
#     i=i+1

#class work , WAP to find out odd and even upto 50.(python code)
#WAP to check 5 is prime number or not ?


num = 11
count = 0
stat = 1

while stat<=num:
    if num%stat == 0:
        count = count + 1
    stat = stat + 1

if count <=2:
    print(f"{num} is prime number")
else:
    print(f"{num} is composite number")


# count=0,stat=1
# count=count+1 = 0+1 = 1
# stat = stat+1 = 1+1 = 2
# stat = stat+1 = 2+1=3
# stat = stat+1 = 3+1=4
# stat= stat+1 = 4+1 = 5
# count=count+1 = 1+1 = 2
# stat =stat+1=5+1=6

