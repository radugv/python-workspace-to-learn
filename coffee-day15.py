# print report: input key <report>
# check resources sufficient? 
# process coin and give change or refund
# check if transaction succesful
# make coffee

from enum import Enum
class Coffee(Enum):
    ESPRESSO = "espresso"        
    CAPPUCCINO = "cappuccino"
    LATTE = "latte"

recipes = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "price": 1.5
    },
    "cappuccino": {
        "water": 250,
        "coffee": 24,
        "milk": 100,
        "price": 3
    },
    "latte": {
        "water": 200,
        "coffee": 24,
        "milk": 150,
        "price": 2.5
    }
}

coins = {
    "penny": 0.01,
    "nickle": 0.05,
    "dime": 0.10,
    "quarter": 0.25 
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def print_report():
    for key in resources.keys():
        if(key == 'water'): print("Water: " + str(resources[key]) + "ml")
        elif(key == 'milk'): print("Milk: " + str(resources[key]) + "ml")
        elif(key == 'coffee'): print("Coffee: " + str(resources[key]) + "g")
        elif(key == 'money'): print("Money: $" + str(resources[key]))

def are_enough_resouces(water, coffee, milk =-1 ):
    if resources["water"] < water:
        print("Sorry. There is not enough water.")
        return False
    elif resources["coffee"] < coffee:
        print("Sorry. There is not enough coffee.")
        return False
    elif milk != -1 and resources["milk"] < milk:
        print("Sorry. There is not enough coffee.")
        return False
    return True

def are_enough_money(money, price):
    if money < price:
        print("You don't have enough money.")
        return False
    return True

def make_coffee(type_of_coffee):
    # check for resouces
    if are_enough_resouces(recipes[type_of_coffee]["water"], recipes[type_of_coffee]["coffee"]) == False:
        return False
    # ask for money
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    given_money = quarters * coins["quarter"] + dimes * coins["dime"] + nickles * coins["nickle"] + pennies * coins["penny"]

    price_of_coffee = recipes[type_of_coffee]["price"]
    if are_enough_money(given_money, price_of_coffee) == False:
        return False
    # prepare espresso
    print("Please enjoy your coffee. Here you have the change: " + str(given_money - price_of_coffee))
    print("Current sum of money: " + str(resources["money"]))
    resources["money"] += price_of_coffee
    print("New sum of money " + str(resources["money"]))
    
def coffee_machine():
    command = input("What would you like? ")

    if(command == 'report'):
        print_report()
    elif(command == Coffee.ESPRESSO.value):
        make_coffee(Coffee.ESPRESSO.value)
    elif(command == Coffee.CAPPUCCINO.value):
        make_coffee(Coffee.CAPPUCCINO.value)
    elif(command == Coffee.LATTE.value):
        make_coffee(Coffee.LATTE.value)


coffee_machine()