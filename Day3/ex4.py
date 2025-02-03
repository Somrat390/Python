print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, L or M? ")
add_peporoni = input("Do you want pepperoni? Y or N? ")
extra_chess = input("Do you want extra chess? Y or N? ")
bill = 0
if size == "S":
    bill += 15
    if add_peporoni == 'Y':
        bill += 2
    if extra_chess == 'Y':
        bill += 1
elif size == "M":
    bill += 15
    if add_peporoni == 'Y':
        bill += 3
    if extra_chess == 'Y':
        bill += 1
elif size == "L":
    bill += 25
    if add_peporoni == 'Y':
        bill += 3
    if extra_chess == 'Y':
        bill += 1

print(f"Your finall bill is ${bill}")


    