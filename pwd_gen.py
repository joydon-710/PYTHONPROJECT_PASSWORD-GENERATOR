import random
print('Hello,Welcome to  Random Password generator!')
# Getting password length
password_len = int(input("Enter the length of the password: "))
if(password_len<=3):
    print("NOT ACCEPTABLE")
    print("The password less than or equal to 3 are not considered as strong passwords")
else:
    print("Which combination of characters you want to insert in your password?")
    
    combination=["uppercase","lowercase","digits","special"];
    #com=[]
#     UPPERCASE=[]
#     LOWERCASE=[]
#     DIGITS=[]
#     SPECIAL=[]
    
    com=input().split()
    for i in com:
        if(i=="uppercase"):
            UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        elif(i=="lowercase"):
            LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        elif(i=="digits"):
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        elif(i=="special"):
            SPECIAL = ['@', '#', '$', '=', ':', '?', '.', '/', '|', '~', '>', '*', '<']
    COMBINED_LIST = DIGITS + UPPERCASE + LOWERCASE + SPECIAL
    password = "".join(random.sample(COMBINED_LIST, password_len))
    print(password)
