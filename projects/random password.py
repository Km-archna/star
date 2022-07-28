# generate a random password

import random
print("Hii, my name is Archana")

def password():
    upper =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    numbers = "012345789"
    symbols = "!@#$%^&*()_+./-=:?"


    string = lower+upper+numbers+symbols
    length = int(input("How many characters do you want your password to be:\n "))

    password = "".join(random.sample(string, length))

    print("Here is your password: ", password)

if __name__ == "__main__":
    while True:
        password()
        choice = input(" do you want the password once again (y/n) ")
        if choice.lower() == 'n':
            break

