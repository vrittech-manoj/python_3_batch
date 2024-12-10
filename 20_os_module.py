import os 

# os.mkdir("new_folder")
# print("you are in dir:",os.getcwd())

# a = os.listdir(os.getcwd())
# print(a)



# Specify the directory to walk
directory_path = "G://"

# Walk through the directory
for dirpath, dirnames, filenames in os.walk(directory_path):
    print(f"Current Directory: {dirpath}")
    print(f"Subdirectories: {dirnames}")
    print(f"Files: {filenames}")
    print("-" * 40)
