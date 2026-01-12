import re
def password_strength(password):
    if len(password)<8:
        print("password is too short")
    elif not re.search("[a-z]",password):
        print("password is too short")
    elif not re.search("[A-Z]",password):
        print("password should have atleast one uppercase letter")
    elif not re.search("[0-9]",password):
        print("password should have atleast one digit")
    elif not re.search("[!@#$%^&*(),.?\":{}|<>]",password):
        print("weak:password should have at least one special charecter.")
    else:
        print("strong password")
user_password=input("enter a password to check its strength:")
password_strength(user_password)