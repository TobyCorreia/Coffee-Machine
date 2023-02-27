MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def deduct_resources(drink):
    global resources
    resources['water'] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]

def calculate_coins():
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total

def transaction(coins, cost):
    if coins >= cost:
        global money
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        money += coins
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def set_coffee(drink):
    deduct_resources(drink)
    print(f"Here is your {drink}. Enjoy!")



machine_on = True
money = 0
while machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        report()
    elif user_input == "off":
        machine_on = False
    else:
        if check_resources(MENU[user_input]["ingredients"]):
            if transaction(calculate_coins(), MENU[user_input]["cost"]):
                set_coffee(user_input)