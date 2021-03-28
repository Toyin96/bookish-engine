filename = "new_file.txt"

my_message = """I'm writing to this file to check if 
                i can read through the file. Hope you understand my pain point"""

try:
    with open(filename, 'w') as fileobject:
        fileobject.write(my_message)
        print("operation successful")
except FileNotFoundError:
    print("Operation not successful")


try:
    with open(filename, 'r') as file:
        content = file.read()
        print(f"i was found {content.lower().count('i')} times in '{filename}'")
except FileNotFoundError:
    print("the operation did not perform successfully")
