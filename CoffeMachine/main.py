menu = {
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
    },
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_available(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def process_coins():
    """returns total calculated from coins inserted"""
    print("Please Insert Coins: ")
    total = int(input("how many quarters: ")) * 0.25
    total += int(input("how many dimes: ")) * 0.1
    total += int(input("how many nickles: ")) * 0.05
    total += int(input("how many pennies: ")) * 0.01
    return total


def process_transaction(money_in, drink_cost):
    if money_in >= drink_cost:
        change = money_in - drink_cost
        print(f"Here is change: {change}$")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded!")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is your {drink_name}")


is_on = True

while is_on:
    user_choice = input("What would you like? (espresso,latte,cappuccino) ").lower()
    if user_choice == "off":
        is_on = False
    elif user_choice == "report":
        print(f"water: {resources['water']}ml" )
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: {profit}$")
    else:
        drink = menu[user_choice]
        if resource_available(drink["ingredients"]):
            payment = process_coins()
            if process_transaction(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])


