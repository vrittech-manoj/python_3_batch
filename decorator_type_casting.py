from decorator_type_casting_1 import conversion

@conversion
def add(a,b):
    print(a+b)

@conversion
def sub(a,b):
    print(a-b)

@conversion
def mul(a,b):
    print(a*b)

add("5","90")
sub("9","6")
mul("2","4")

#WAP to make your own decorator for 