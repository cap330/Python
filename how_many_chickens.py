chicken_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

def print_how_many(ammount, animals):
    if ammount == 1 or animals == 'sheep':
        print(ammount, animals)
    else:
        print(ammount, animals + 's')


def max_can_buy(price):  
    global chicken_price, goat_price, pig_price, cow_price, sheep_price
    if price >= sheep_price:
        ammount = money // sheep_price
        print_how_many(ammount, 'sheep')
    elif money >= cow_price:
        ammount = money // cow_price
        print_how_many(ammount, 'cow')
    elif money >= pig_price:
        ammount = money // pig_price
        print_how_many(ammount, 'pig')
    elif money >= goat_price:
        ammount = money // goat_price
        print_how_many(ammount, 'goat')
    elif money >= chicken_price:
        ammount = money // chicken_price
        print_how_many(ammount, 'chicken')     
    else:
        print('None')


money = int(input())
max_can_buy(money)
