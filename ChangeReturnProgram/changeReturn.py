__author__ = 'anthonymace'

def enter_cost_of_item():
    cost = float(input("Enter cost: "))
    print("Cost was: ", cost)
    return cost

def enter_payment_amount():
    payment_amount = float(input("Enter payment amount: "))
    print("Payment was: ", payment_amount)
    return payment_amount

def is_payment_enough(cost, payment):
    return payment > cost

def calc_difference(cost, payment):
    return payment - cost

def return_bills(difference):
    hundreds = 0
    fifties = 0
    twenties = 0
    tens = 0
    fives = 0
    ones = 0

    while difference >= 100:
        hundreds += 1
        difference -= 100

    while difference >= 50:
        fifties += 1
        difference -= 50

    while difference >= 20:
        twenties += 1
        difference -= 20

    while difference >= 10:
        tens += 1
        difference -= 10

    while difference >= 5:
        fives += 1
        difference -= 5

    while difference >= 1:
        ones += 1
        difference -= 1

    return hundreds * 100, fifties * 50, twenties * 20, tens * 10, fives * 5, ones

def return_coins(difference):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    while difference >= 0.25:
        quarters += 1
        difference -= 0.25

    while difference >= 0.1:
        dimes += 1
        difference -= 0.1

    while difference >= 0.05:
        nickels += 1
        difference -= 0.05

    while difference >= 0.01:
        pennies += 1
        difference -= 0.01

    return quarters, dimes, nickels, pennies

def add_bills(bills):
    return bills[0] + bills[1] + bills[2] + bills[3] + bills[4] + bills[5]


def main():
    cost = enter_cost_of_item()
    payment = enter_payment_amount()
    if is_payment_enough(cost, payment):
        difference = calc_difference(cost, payment)
        bills = return_bills(difference)
        bills_total = add_bills(bills)
        print(bills)
        print(bills_total)

main()