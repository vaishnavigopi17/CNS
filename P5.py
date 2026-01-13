import re
def check_password_strength(password):
    if len(password)<8:
        return "weak:password should be atleast 8 charecters."
    if not re.search("[a-z]",password):
        return "weak:password should haveat least one lower case letter."
    if not re.search("[A-Z]",password):
        return "weak:password should haveat least one upper case letter."
    if not re.search("[0-9]",password):
        return "weak:password should haveat least one digit."
    if not re.search("!@#$%^&*(),.?\":{}|<>]",password):
        return "weak:password should haveat least one special charecter."
    return "strong password"
password=input("enter the password:")
print(check_password_strength(password))