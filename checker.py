import string

special = list(string.punctuation)
characters = 0
digits = 0
upper = 0
lower = 0

password = input("Enter password: ")

if(len(password)<8):
    print("Password should be 8 characters!")
elif(len(password)>8):
    for char in password:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            if char.isupper():
                upper += 1
            elif char.islower():
                lower +=1