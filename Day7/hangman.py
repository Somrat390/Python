
import random
import hangmanpic
import word

#step1 

chosen_word = random.choice(word.HANGMAN_WORDS)

Live = 6
print(f"Pssst, the solution is {chosen_word}.")
display = []
length = len(chosen_word)
for space in range(len(chosen_word)):
    display += '_'

while '_' in display:
    guess = input("Guess a letter ").lower()
    
    if guess in display:
        print(f"You have already guessed {guess}")

    for position in range(length):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    if guess not in display:
        print("You losse a life😔")
        print(hangmanpic.HANGMAN_PICS[Live])
        Live -= 1
    
    if Live == 0:
        print(hangmanpic.HANGMAN_PICS[Live])
        print("You Lose")
        quit()
    
if Live == 6:    
    print("You won")

