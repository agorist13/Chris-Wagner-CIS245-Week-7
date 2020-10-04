
import os
import json

def get_user_dir():
    while True:
        user_dir = input("Please enter the name of the directory you wish to use: ")
        if os.path.isdir(user_dir):
            print("Your directory exists.")
            break
        else:
            print("The directory you entered doesnt exist. "
                  "Please enter a different directory name.")
    return user_dir

def get_file_name():
    file_name = input("Please enter the name of the file you would like to create: ")
    return file_name

def get_user_info():
    user_name = input("What is your name? ")
    user_address = input("What is your address? ")
    user_phoneNumber = input("What is your phone number? ")
    return str(user_name + ", " + user_address + ", " + user_phoneNumber)

def get_complete_path():
    completePath = get_user_dir() + "/" + get_file_name() + ".json"
    return completePath

def main():

    completePath = get_complete_path()
    user_info = get_user_info()

    with open(completePath, 'w') as f_obj:
        json.dump(user_info, f_obj)

    with open(completePath) as f_obj:
        user_data = json.load(f_obj)
        print(f"\nNew User Info:"
              f"\n{user_data}")


main()