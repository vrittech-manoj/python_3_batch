class Animal:

    def base(self):
        print("i am Animal")

class Dog(Animal):
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"my name is {self.name}")

class Cat(Animal):
    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"my name is {self.name}")

dog_obj = Dog("chuchu")
dog_obj.base()
dog_obj.display()


cat_obj = Cat("tom")
cat_obj.base()
cat_obj.display()


    