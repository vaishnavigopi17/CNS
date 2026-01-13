import hashlib
def get_sha256_hash(text): 
    sha_signature=hashlib.sha256(text.encode()).hexdigest()
    return sha_signature
text="cyber security is important!"
print(f"text:{text}")
print(f"SHA-256 Hash:{get_sha256_hash(text)}")
