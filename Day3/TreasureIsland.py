print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("\t\tWelcome to Treasure Island.\n")
print("Your mission to find the treasure.\n")
path = input('You\'re at a cross road, Where do you want to go? Type "Left" or "Right" \n').lower()
if path == "left":
    path2 = input('''"You come to a lake. There is an island in the middle of the lake.Type "wait" to wait for boat.Type "swim" to swim across.\n''').lower()
    if path == "wait":
       colour = input("You arrive at the island unharmed.There is a house with 3 doors.One red, one yellow and one blue.Which colour do you choose? \n").lower()
       if colour == "yellow":
           print("You found the treasure! You won")
       elif colour == "red":
           print("It's a room full of fire. Game over.")
       elif colour == "blue":
           print('You enter a room of a beasts. Game over.')
    else:
        print("You got attacked by an angry trout.Game over.")
else:
    print("You fell into a hool . Game over.")
    
