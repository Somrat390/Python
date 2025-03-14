programming_dictionary = {
    "Bug": "An error in program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again"
    }

print(programming_dictionary["Bug"])

# programming_dictionary["math"] = "Math is easy"

# print(programming_dictionary)

# programming_dictionary = {}
# print(programming_dictionary)

programming_dictionary["Bug"] = "Bug"
print(programming_dictionary)

# loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
