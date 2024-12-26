#class constructor 


class Chrismas:
    welcome_text = "Every one welcome on chrismas party"
 

    def __init__(self,a , b,c=None):
        print("this will automatic called when object is created")
        self.a = a 
        self.b = b
        self.c = c
 

    def check_authorize_person(self):
        print("he is authtorize")

obj1 = Chrismas(4,9)
obj2 = Chrismas(1,2)

print(obj1.a,obj2.a)


