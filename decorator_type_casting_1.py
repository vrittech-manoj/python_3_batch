def conversion(func):
    def inner(a,b):
        a = int(a) 
        b = int(b) 
        return func(a,b)
    return inner