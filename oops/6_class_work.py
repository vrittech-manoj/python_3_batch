employe_datas = [
        {'name':"ram",'salary':35000,'bonus':2},
        {'name':"shyam",'salary':30000,'bonus':5},
        {'name':"hari",'salary':80000,'bonus':10},
        {'name':"gopal",'salary':620000,'bonus':23},
    ]





class Employee:
    def __init__(self,name,salary,bonus):
        self.user_name = name 
        self.salary = salary
        self.bonus = bonus 

    def calculate_salary(self):
        output = self.salary+self.bonus/100*self.salary
        return output
    


    

for emp_data in employe_datas:
    print("******************")
    emp_obj =  Employee(emp_data['name'],emp_data['salary'],emp_data['bonus'])
    output = emp_obj.calculate_salary()
    print(f"{emp_data['name']} total salary ith bonus ",output)


