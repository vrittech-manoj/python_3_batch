class Calculator:

    def __init__(self,first_number,operator,second_number):
        print("this is initializing....")
        self.first_number = first_number
        self.second_number = second_number
        self.operator = operator

    def result(self):
        if self.operator == "+":
            return self.add()
        elif self.operator == "-":
            return self.susbtract()

    def add(self):
        return self.first_number + self.second_number
    
    def susbtract(self):
        return self.first_number - self.second_number


cal_obj = Calculator(9,"+",8) 
output = cal_obj.result()

print("calculation of two number is ",output)
