import random
import time
import os

money = 1000


while True:

    os.system("cls")
    print(f"You currently have {money}$ in your wallet")
    bettingMoney = int(input('How much money do you wanna Bet ? : '))

    if bettingMoney > money:
        print("You don't have enough money")


    elif bettingMoney < money:
        money = money - bettingMoney
        print(f"You have betted {bettingMoney} $")
        time.sleep(1)
        print("Wait till its loading...")
        time.sleep(3)
        choice = random.randint(1,2)
        
        if choice == 1:
            print("You won")
            time.sleep(1)
            money = money + 2*(bettingMoney)
            print(f"Now you have {money} $")
            time.sleep(2)    
            
        elif choice == 2:
            print("You loss")
            time.sleep(1)
            print(f"Now you have {money} $")
            time.sleep(2)
            