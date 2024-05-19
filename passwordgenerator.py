import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
while True:
    try:
        length = int(input("Enter the desired length of the password: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
password = generate_password(length)
print("Generated password:", password)
