name1 = input("name1 = ").upper()
name2 = input("name2 = ").upper()

Totall1 = name1.count("T") + name1.count("R") +name1.count("U") + name1.count("E")
Totall1 += name2.count("T") + name2.count("R") +name2.count("U") + name2.count("E")

Totall2 = name1.count("L") + name1.count("O") +name1.count("V") + name1.count("E")
Totall2 = name2.count("L") + name2.count("O") +name2.count("V") + name2.count("E")

Love_score = str(Totall1) + str(Totall2)
Love_score = int(Love_score)
if Love_score < 10 or Love_score > 90:
    print("Your score is x, you go together like coke and mentos")
elif 40 <= Love_score <= 50:
    print("Your score is Y, you are alright together")
else:
    print("Your Score is z")