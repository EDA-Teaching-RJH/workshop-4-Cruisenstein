
wallet = 0

while wallet < 75:

    if wallet >= 75:
        break
    else:
        print("------PLEASE ENTER 75p TO BEGIN.------")
        print(f"You have {wallet}p in credit")
        more = int(input("Please enter a coin: "))

        match more:
            case 5 | 10 | 20 | 50:
                print("Coin Accepted")
                wallet += more
            case _:
                print("This machine only accepts 50p, 20p, 10p & 5p coins.")

print("---------MENU---------")
print("1: Americano:     70p")
print("2: Mocha:         75p")
print("3: Latte:         70p")
print("4: Iced Latte:    75p")
print("5: Hot Cholocate: 55p")
print(f"-----CREDIT: {wallet}p-----")
pick = int(input("Please make a selection using the numbers: "))

match pick:
    case 1:
        print("------Thank you, enjoy your Americano.------")
        purhase = 70
    case 2:
        print("------Thank you, enjoy your Mocha.------")
        purhase = 75
    case 3:
        print("------Thank you, enjoy your Latte------")
        purhase = 70
    case 4:
        print("------Thank you, enjoy your Iced Latte.------")
        purhase = 75
    case 5:
        print("------Thank you, enjoy your Hot Chocolate.------")
        purhase = 55
    case _:
        print("That's not on the menu!")

wallet = wallet - purhase
print(f"Your change is {wallet}p")



    
       