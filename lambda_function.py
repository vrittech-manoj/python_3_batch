# add = lambda first_number:first_number**2
# print(add(5))


# def add(a,b):
#     return a+b

# print(add(5,3))
numbers   = [1,5,8,3]

def square(x):
    return x*x

squared = list(map(lambda x:x**2,numbers))
print(squared)