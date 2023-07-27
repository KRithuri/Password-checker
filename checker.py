import string

special = list(string.punctuation)
characters = 0
digits = 0
upper = 0
lower = 0

password = input("Enter password: ")

if(len(password)<8):
    print("Password should be 8 characters!")