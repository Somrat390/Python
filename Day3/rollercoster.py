print("Welcome to the roollercoster!")
height = int(input("What is your height in cm?? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket is $5 ")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7 ")
    else:
        bill = 12
        print("Adult ticket is $5 ")
    wants_photo = input("Do you want photo? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your finall bill is ${bill}")
  
else:
    print("Sorry, you have to grow taller before you can ride")