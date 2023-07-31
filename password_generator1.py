# Here I just tried to reduce the code size and make it simple but still performing the same task
import random
import string


def password_generator():
    length = int(input("Enter the desired length of the password: "))
    password = ''.join(random.choices(string.ascii_letters +
                       string.digits + string.punctuation, k=length))
    print("Generated Password:", password)


password_generator()
