""" 
THINGS TO ADD
    * Get rid of enter file name for needing another password
    * Fix 'Enter enrypted password' (might be possible with a database)
    * Error checking
    * Eventually, add stronger encryption

"""

import string

def main():
    def initialPass():
        password = "P@$$W0RD4515"
        userInput = input("Enter password: ")
        while (userInput != password):
            print("Wrong password.")
            userInput = input("Re-enter password: ")
        if userInput == password:
            passGrabber()
    def passGrabber():
        def decryptor():
            print("Decryptor beginning.")
        
        def searchWord():
            data_sheet = input("Enter file name: ")
            word = str(input("Enter web address/username: "))
            with open(data_sheet, "r") as fp:
                lines = fp.readlines()
                for line in lines:
                    if line.find(word) != -1:
                        print("\n")
                        print(line)
                        print("\n")
        def decryptor():
            def caesar(text, shift, alphabets):
                def shift_alphabet(alphabet):
                    return alphabet[shift:] + alphabet[:shift]

                shifted_alphabets = tuple(map(shift_alphabet, alphabets))

                final_alphabet = ''.join(alphabets)
                final_shifted_alphabet = ''.join(shifted_alphabets)
                table = str.maketrans(final_alphabet, final_shifted_alphabet)

                return text.translate(table)
            decrypt = str(input("Enter encrypted password: "))
            print(caesar(decrypt, 26-7, [string.ascii_lowercase, string.ascii_uppercase]))
        searchWord()
        decryptor()

        again = input("Need another password? <y/n>: ")
        if again == "y":
            passGrabber()
        else:
            print("Goodbye.")
            return     
    initialPass()
main()