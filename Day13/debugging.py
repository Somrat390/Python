#Describe the problem

# def my_function():
#     for i in range(1,21):
#         if i == 20:
#             print("You got it")

# my_function()

# Reproduce the Bug

# from random import randint
# dice_img = ["1", "2", "3", "4", "5", "6"]
# dice_num = randint(0,5)
# print(dice_img[dice_num])

############# Play computer

# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#     print("You are a millenial")
# elif year >= 1994:
#     print("You are a Gen Z")

########### Fix the error
# age = input("How old are you? ")
# if age > 18:
#     print("You can drive at age {age}")

# ###########3 Print is your friend
# pages = 0
# words_per_page = 0
# pages = int(input("Number of pages: "))
# words_per_page == int(input("Number of words per page: "))
# total_words = pages * words_per_page
# print(total_words)

############3 Use a debugger

def mutable(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutable([1,2,3,4,58,13])