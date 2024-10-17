wallet = 0

while wallet < 75:

    if wallet >= 75:
        break
    else:
        print("------A coffee costs 75p.------")
        print(f"You have {wallet}p in credit")
        more = int(input("Please enter a coin: "))

        match more:
            case 5 | 10 | 20 | 50:
                print("Coin Accepted")
                wallet += more
            case _:
                print("Error invaild input")
                print("this machine only accepts 50p, 20p, 10p & 5p coins.")

wallet = wallet - 75
print("------Thank you, enjoy your coffee.------")
print(f"           Your change is {wallet}p")



    
       