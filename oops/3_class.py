class Calculator:
    output_sentence = "of two number is"
    
    def sum(self,a,b):
        print("addition" , self.output_sentence,a+b)

    def subtract(self,a,b):
        print("subtraction of two number is :",a-b)

    def multiply(self,a,b):
        print("subtraction of two number is :",a*b)


c1 = Calculator()
c1.sum(5,10)

