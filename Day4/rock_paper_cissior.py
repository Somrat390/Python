import random
rock = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = ''' 
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

user = int(input('What do you choose?Type 0 for Rock, 1 for Paper or 2 for Scissors.'))

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissor)
else:
    print("Chosse correct option")
    quit()

game =[rock, paper, scissor]
len = len(game) - 1
computer_chose = random.randint(0,len)
print(f"Computer chose:\n{game[computer_chose]}")

if user == 0 and computer_chose == 2:
    print("You Won")
elif user == 1 and computer_chose == 0:
    print("You won")
elif user == 2 and computer_chose == 1:

    print("You Won")
elif user == computer_chose:
    print("Draw")
else:
    print("You Lose")