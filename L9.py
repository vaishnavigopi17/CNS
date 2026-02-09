import hashlib
def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()
data=input("enter data to send:")
hash_value=generate_hash(data)
print("generated hash:",hash_value)
recieved_data=input("enter recieved data:")
recieved_hash=generate_hash(recieved_data)
if recieved_hash==hash_value:
    print("integrity verified: data not modified")
else:
    print("integreti failed: data modified")