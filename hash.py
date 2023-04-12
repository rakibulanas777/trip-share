import hashlib

# password encodeing
email = "rakibulanas777@gmail.com"
pwd = "AsdfikLm@@129"
pwd_encode = pwd.encode()

pwd_hash = hashlib.md5(pwd_encode).hexdigest()

your_email = "rakibulanas777@gmail.com"
your_pwd = "AsdfikLm@@129"

hashed_your_password = hashlib.md5(your_pwd.encode()).hexdigest()
if (email == your_email and pwd_hash == hashed_your_password):
    print("right user")
else:
    print("wrong user")
print(pwd)
print(pwd_hash)
