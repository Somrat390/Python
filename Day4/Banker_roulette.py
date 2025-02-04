import random

name_string = input("Give me everybody's names, separated by a comma. ")
names = name_string.split(",")

len = len(names)
random_choice = random.randint(0,len-1)


person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} will pay the bill today")

person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} will pay the bill today")
