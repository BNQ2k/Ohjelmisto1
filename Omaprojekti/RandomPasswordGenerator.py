import random
print("Your password: ")
kirjaimetnumerotmerkit = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#=?+"
password = ""
for x in range(20):
    password += random.choice(kirjaimetnumerotmerkit)
print(password)