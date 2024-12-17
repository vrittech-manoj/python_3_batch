welcome_message = """
        WELCOME TO MY STUDENT MANAGEMENT SOFTWARE
        PRESS NUMBER?
        1) Add new student
        2) read all student
        3) search student
        4) delete student
    """
total_student = []

def add_student():
    name = input("Enter student name#>>>")
    number = input("Enter student number#>>>")
    data = {"name":name,"number":number}
    total_student.append(data)

def search():
    pass 

def delete():
    pass 

def display_all_student():
    pass 

while True:
    print(welcome_message)
    user_input = input("Enter option #>>>")
    if user_input == "1":
        add_student()
    elif user_input == "2":
        display_all_student()
    elif user_input == '3':
        search()
    elif user_input == '4':
        delete()
