import os
import string
import random
import hashlib
import binascii
"""
    add_user.py - Stores a new username along with salt/password

    CSCI 3403
    Authors: Matt Niemiec and Abigail Fernandes
    The solution contains the same number of lines (plus imports)
"""
user = input("Enter a username: ")
password = input("Enter a password: ")

# TODO: Create a salt and hash the password


def randomStringDigits(stringLength=10):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

salt = hashlib.sha256(os.urandom(3)).hexdigest().encode('ascii')
print(salt)
print("SALT")

def hash_password(password):
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

hashed_password = hash_password(password)
print(hashed_password);


#hash = hashlib.pbkdf2_hmac('sha256', bitPassword.encode('utf-8'),salt,100);#gets hash I think why
    #https://nitratine.net/blog/post/how-to-hash-passwords-in-python/
    # Convert the password to bytes (.encodeUtf8)
    # It is recommended to use at least 100,000 iterations of SHA-256



try:
    reading = open("passfile.txt", 'r')
    for line in reading.read().split('\n'):
        if line.split('\t')[0] == user:
            print("User already exists!")
            exit(1)
    reading.close()
except FileNotFoundError:
    print("File not found");

with open("passfile.txt", 'a+') as writer:
    writer.write("{0}\t{1}\t{2}\n".format(user, salt, hashed_password))
    print("User successfully added!")
