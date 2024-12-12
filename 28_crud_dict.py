# crud 

# c = create 
# r = read
# u = update 
# d = delete 

# data_1 = {'name':"ram","age":15,"number":980080}
# data_2 = {'name':"shyam","age":15,"number":980080}
# data_3 = {'name':"hari","age":15,"number":980080}

# total_data = [data_1,data_2,data_3]
# # print(total_data)
# search_value = input("Enter what to search?#>>>")
# for item in total_data:
#     if search_value == item['name']:
#         print("search found!!! ",item)


welcome_message = """
    WELCOME TO MY STUDENT MANAGEMENT SOFTWARE
    PRESS NUMBER?
    1) Add new student
    2) read all student
    3) search student
    4) delete student
"""
print(welcome_message)
user_input = input("Enter option #>>>")
if user_input == "1":
    name = input("Enter student name#>>>")
    roll = input("Enter student roll#>>>")
    #add student data to dictionary and then append to list

elif user_input == "3":
    search_student = input("What to search?#>>>")
    
