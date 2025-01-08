from new_folder.shape import Shape

class Square(Shape):
    def perimeter(self):
        print("perimeter of square is 4*a")

    def area(self,a):
        print("Area of square is ",a*a) 

square_obj = Square()
square_obj.fact()
square_obj.area(4)


# write a program to overide of parent class method in child class

