dollarAmount = 11.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def cash_to_coins(amt):
    quarters = amt // .25
    piggyBank["quarters"] = quarters
    diff = amt - (quarters * .25)

    dimes = diff // .1
    piggyBank["dimes"] = dimes
    diff = diff - (dimes * .1)

    nickels = diff // .05
    piggyBank["nickels"] = nickels
    diff = diff - (nickels * .05)

    pennies = diff // .01
    piggyBank["pennies"] = pennies
    diff = diff - (pennies * .01)

    print(piggyBank)

cash_to_coins(dollarAmount)