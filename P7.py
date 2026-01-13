def is_password_common(password:str,common_password:list)->bool:
    return password in common_password
common_passwords=['123456','password','123456789','qwerty','abc123']
password='password1234'
if is_password_common(password,common_passwords):
    print("password is too common!")
else:
    print("password is not in the common list")
