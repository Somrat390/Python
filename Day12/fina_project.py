import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, computed_num, turns):
    if guess == computed_num:
        print(f"You got it! The answer was {computed_num}")
    elif guess > computed_num:
        print("Too High.")
        turns -= 1
    else:
        print("Too Low.")
        turns -= 1

def set_dificulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        turns = EASY_LEVEL_TURNS
    else:
        turns = HARD_LEVEL_TURNS
    

def game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    computed_num = random.randint(1,100)

    turns = set_dificulty()
    
    guess = 0

    while guess != computed_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, computed_num, turns)
        if turns == 0:
            print("You have run out of guess! You loose.")
            return
        elif guess != computed_num:
            print("Guess Again")


game()






############################# This is my code and above was angela code diffrence is betwween keep function




# level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# if level == 'easy':
#     number_of_attemp = 10
#     for i in range(10):
#         print(f"You have {number_of_attemp} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#         if guess == computed_num:
#             print("You win!")
#             break
#         elif guess > computed_num:
#             print("Too High.")
#         else:
#             print("Too Low.")
        
#         number_of_attemp -= 1

#         if number_of_attemp < 1:
#             print("You have no chance to guess. You loose")
#         else:
#             print("Guess Again.")
        

# elif level == "hard":
#     number_of_attemp = 5
#     for i in range(5):
#         print(f"You have {number_of_attemp} attempts remaining to guess the number.")
#         guess = int(input("Make a guess: "))
#         if guess == computed_num:
#             print("You win!")
#             break
#         elif guess > computed_num:
#             print("Too High.")
#         else:
#             print("Too Low.")

#         number_of_attemp -= 1

#         if number_of_attemp == 0:
#             print("You have no chance to guess. You loose")
#         else:
#             print("Guess Again.")
        
# else:
#     print("Enter a valid level")

