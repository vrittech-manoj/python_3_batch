class Person:
    def __init__(self,gender):
        self.gender = gender

    def get_gender(self):
        print(f"I am gender {self.gender} and my name is {self.name}")

class Student(Person):
    def __init__(self,name,gender):
        self.name = name
        # Person.__init__(self)
        super().__init__(gender)
    
    def study(self):
        print(f"my name is {self.name} and i am studying")

ram_obj = Student("Ram","male")
ram_obj.study()
ram_obj.get_gender()
print(ram_obj.gender)

# shyam_obj  = Student("Shyam")
# shyam_obj.study()




