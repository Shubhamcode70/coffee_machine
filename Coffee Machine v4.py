from coffeeart import logo
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

money = 0
print(logo)

def resource_check(coffee_require):
    for item in coffee_require:
        if coffee_require[item] > resources[item]:
            print(f"Coffee Machine Doesn't have enough {item}")
            return False
    return True

def coin_process():
    coins = {"quarter": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}
    for i in coins:
        coins_value = int(input(f"How many {i} ? : $"))
        coins[i] *= coins_value

    drawer = []
    for coin_value in coins:
        drawer.append(coins[coin_value])

    total = sum(drawer)
    return total

def make_coffee(customer_order,payment,resource_check):
    if payment == True and resource_check == True:
        for item in coffee_require:
            resources[item] = resources[item] - coffee_require[item]
            
        print(f"Here is your {customer_order} ☕️. Enjoy!")

def transaction_process(payment_in, coffee_price):
    if payment_in >= coffee_price:
        exchange = round(payment_in - coffee_price, 2)
        print(f"Please collect your change ${exchange}")
        global money 
        money += coffee_price
        return True
    else:
        print(f"Transaction failed due to insufficient money {payment} refunded!")
        return False


machine_on = True
while machine_on:
    customer_order = input("What would you like? (espresso/latte/cappuccino) : ")
    if customer_order == "off":
        machine_on = False
    elif customer_order == "report":
        print("The current resource values")
        print(f" Water : {resources['water']}ml")
        print(f" Milk : {resources['milk']}ml")
        print(f" Coffee : {resources['coffee']}gm")
        print(f"Money in Drawer : {money}")
    else:
        s_coffee = MENU[customer_order] #Got the user Coffee from the list of dict
        coffee_require = s_coffee["ingredients"]
        coffee_cost = s_coffee["cost"]
        
        if resource_check(coffee_require):
            payment = coin_process()
            check_transaction = transaction_process(payment, coffee_cost)
            check_res = resource_check(coffee_require)
            make_coffee(customer_order, check_transaction, check_res)
