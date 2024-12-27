class Notes:
    def append_notes(self):
        id = input("Enter computer id#>>>") #id,name,price,brand,quantity
        name = input("Enter computer name#>>>")
        full_detail = f"{id},{name}"
        with open("notes.txt",'a') as file_obj:
            file_obj.write("\n"+full_detail)

    def display_notes(self):
        with open("notes.txt",'r') as file_obj:
            data = file_obj.read()
            print(data)

    def search(self):
        search_item = input("what to search id?#>>>")
        print(f"searching {search_item} ....")
        with open("notes.txt",'r') as file_obj:
            all_datas = file_obj.readlines()
        
        for item in all_datas:
            splitted_item = item.split(",")
            # print(splitted_item)
            if search_item in splitted_item[0]:
                print("*****************search founds congrats !",item)
    

notes_obj = Notes()
while True:
    print("""
        1:append notes
        2:display notes
        3:search
        """)
    menu_input = input("Enter menu#>>>")
    if menu_input == "1":
        notes_obj.append_notes()
    elif menu_input == "2":
        notes_obj.display_notes()
    elif menu_input == "3":
        notes_obj.search()



