import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
Symbols = ['!', '#', '$', '%', '&','(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
for char in range(0,nr_letters):
    password.append(random.choice(letters))

for char in range(0,nr_symbols):
    password.append((random.choice(Symbols)))

for ch in range(0,nr_numbers):
    password.append(random.choice(Numbers))
    
random.shuffle(password)

password = "".join(password)

print(f"Your Password is {password}")




