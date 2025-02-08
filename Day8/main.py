def greet():
    print("this is the first function")
    print("Enter the name of the function")
    print("Print the function")

greet()


def greet_with_name(name):
    print(f"Hi {name}")
    print(f"How do you do {name}")

greet_with_name("Somrat")

def greet_with(name, location):
    print(f"Hi {name}")
    print(f"Where are you at {location}")

greet_with("Somrat", "Dhaka")

greet_with(location="New York", name="Sum")