def is_prime(number):
    for i in range(2,number):
        if number%i == 0:
            return False
       
    return True
        
a = 9
check_prime = is_prime(a)
if check_prime == True:
    print(f"{a} is prime number")
else:
    print(f"{a} is composite number")


# def is_even(number):
#     if number%2==0:
#         return True
#     else:
#         return False

# a = 6
# check_even = is_even(a)
# if check_even == True:
#     print(f"{a} is even number")
# else:
#     print(f"{a} is odd number")