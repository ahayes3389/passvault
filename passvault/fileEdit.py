"""
THINGS TO ADD
    * Add confirmation input to all options
    * Finish 1, edit a login
    * Make sure it works
    * Make the display 'pretty' and easy to read
    * Make password plain text when confirming
    * Error checking and checking for duplicates
    * Add option to cancel selection when confirming
    * Eventually, encorporate stronger encryption used in passvault main code
"""

import string

def caesar(text, shift, alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))

    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)

    return text.translate(table)

main_file = input("Enter file name: ")
breaker = False
while breaker != True:
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Edit a login\n2. Add a login\n3. Delete a login\n4. View saved passwords\n0. Exit program")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    answer = int(input("Enter an option from the list above: "))
    

# Option 1
    if answer == 1:
        openFile = open(main_file, "w")

# Option 2
    elif answer == 2:
        openFile = open(main_file, "a")
        answer = "y"
        while (answer == "y"):
            confirm = "n"
            while (confirm == "n"):
                webName = input("Enter web address: ")
                userName = input("Enter username: ")
                password = input("Enter password: ")
                password = caesar(password, 7, [string.ascii_lowercase, string.ascii_uppercase])
                print("Website: ", webName, "Username: ", userName, "Password: ", password)
                confirm = input("Confirm? <y/n>: ")
                if confirm == "y":
                    openFile.write(webName + ":" + userName + ":" + password + "\n")
            answer = input("Would you like to enter another login? <y/n>: ")

            if answer == "n":
                openFile.close()

# Option 3
    elif answer == 3:
        confirm = "n"
        while (confirm == "n"):
            word = str(input("Enter web address/username: "))
            with open(main_file, "r") as fp:
                lines = fp.readlines()
                for line in lines:
                    if line.find(word) != -1:
                        print("\n")
                        print(line)
                        print("\n")
                delete_value = input("Enter the string to delete: ")
                print(line)
            confirm = input("Confirm deletion? <y/n>: ")
            if confirm == "y":
                with open(main_file, "r") as f:
                    file = f.readlines()
                with open(main_file, "w") as f:
                    for line in file:
                        words = line.strip("\n").lower().split(" ")
                        if delete_value.lower() not in words:
                            f.write(line)

# Option 4
    elif answer == 4:
        with open(main_file) as f:
            print("\n*********************")
            print(f.read())
            print("*********************")

# Option 5
    elif answer == 0:
        print("Goodbye.")
        breaker = True

    else:
        print("ERROR: option not recognized.")
        answer = int(input("Re-enter option: "))
