from manu import MENU ,resource

is_one = True
profit = 0

def print_report():
    print(f"""
    Water: {resource["water"]}ml
    Milk: {resource["milk"]}ml
    Coffee: {resource["coffee"]}g
    Money: ${profit}
    """)

def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resource[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    print("Please insert coin.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickels?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        if change > 0:
            print(f"Here is your ${change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")

def make_coffe(drink_name, order_ingredient):
    for item in order_ingredient:
        resource[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}🍵")


while is_one:
    choice = input("What would you like?(espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_one = False
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])



