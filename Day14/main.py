from art import logo, vs
from game_data import data
import random
import os

score = 0
def get_random_account():
    """get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into a printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    print(f"{name}: {account["follower_count"]}")
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'




def game():
    print(logo)
    score = 0
    game_should_continue = True
    accout_A = get_random_account()
    accout_B = get_random_account()
    
    while game_should_continue:
        accout_A = accout_B
        accout_B = get_random_account()

        while accout_A == accout_B:
            accout_B = get_random_account()
    
        print(f"Compare A: {format_data(accout_A)}.")
        print(vs)
        print(f"Against B: {format_data(accout_B)}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = accout_A["follower_count"]
        b_follower_count = accout_B["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system("cls")
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

game()




