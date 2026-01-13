import itertools
import string 

def brute_force_password(password,max_length=4):
    charecters=string.ascii_letters+string.digits
    for length in range(1,max_length+1):
        for guess in itertools.product(charecters,repeat=length):
            guess=''.join(guess)
            if guess==password:
                return f"password'{password}'cracked in {length} tries!"
password="abc1"
print(brute_force_password(password))
