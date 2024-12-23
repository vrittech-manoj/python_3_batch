employe_datas = [
        {'name':"ram",'salary':35000,'bonus':2},
        {'name':"shyam",'salary':30000,'bonus':5},
        {'name':"hari",'salary':80000,'bonus':10},
        {'name':"gopal",'salary':620000,'bonus':23},
    ]

#WAP to calculate staff salary with bonus , and print staff name and total salary 
#any way

# class Employee:
#     pass

def total_salary(salary,bonus):
    return salary + bonus/100*salary

for item in employe_datas:
    name = item['name']
    salary = item['salary']
    bonus = item['bonus']
    total_salary_var = total_salary(salary,bonus)
    print("************************")
    print(f"staff name {name} with salary {salary} , bonus {bonus}% , total salary {total_salary_var}")

