import os 

# print(os.getcwd()) # get current working directory
# print(os.path.abspath(__file__)) # get absolute path of the current file
# print(os.path.dirname(os.path.abspath(__file__))) # get the directory name of the current file
# print(os.listdir()) # list all files and directories in the current directory

# for i in os.listdir():
#     if os.path.isfile(i):
#         print(f"{i} is a file")
#     elif os.path.isdir(i):
#         print(f"{i} is a directory")

last_load = "2026-01-14"
for i in os.listdir((os.path.join(os.path.dirname(os.path.abspath(__file__)),"Data"))):
    if i.split(".")[0] > last_load:
        # Logic to process the file
        print(f"Processing {i} new file")