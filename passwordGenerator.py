import string
import random

print("Password Lenght:")
Lenght = int(input())
print(Lenght)
randomString = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_letters + string.ascii_lowercase + string.punctuation, k = Lenght))
print(randomString)


