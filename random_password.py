import string
import random

password_length = int(input("enter a length of password"))

characters = string.ascii_letters + string.digits + string.punctuation

random_characters = random.choice(characters)

password = ""

for _ in range(password_length):
    ccharactor = random.choice(characters)
    password = password + ccharactor

print(password)