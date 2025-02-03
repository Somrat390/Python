print("Welcome to the roollercoster!")
height = int(input("What is your height in cm?? "))

if height >= 120:
    print("You can ride the rollercoster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5 for ticket")
    elif 12 <= age <= 18:
        print('Please pay $7 for ticket')
    else:
        print("Please pay $12 for ticket")
else:
    print("Sorry, you have to grow taller before you can ride")