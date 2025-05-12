import os
import random
import time

symbols = ['💎', '💀', '💲']
balance = 0
MIN_DEPOSIT = 100
MAX_DEPOSIT = 10000
MIN_BET = 10

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(rows):
    for row in rows:
        print(" | ".join(f"{s:^3}" for s in row))

def spin_slot_machine(spins=20, delay=0.17):
    """
    Spins the slot machine and returns the middle row (list of 3 symbols).
    
    :param spins: Number of spin cycles before stopping.
    :param delay: Delay between spins (in seconds).
    :return: List of 3 symbols (middle row).
    """
    for _ in range(spins):
        clear()
        rows = [[random.choice(symbols) for _ in range(3)] for _ in range(3)]
        print("  🎰 Spinning... 🎰\n")
        print_grid(rows)
        time.sleep(delay)

    clear()
    final_rows = [[random.choice(symbols) for _ in range(3)] for _ in range(3)]
    print("  🎰 SPIN RESULT 🎰\n")
    print_grid(final_rows)

    middle_row = final_rows[1]
    print("\nResut:", " | ".join(f"{s:^3}" for s in middle_row))

    return middle_row


def wlc_screen (): 
    clear()
    print("🎰 WELCOME TO SLOT MACHINE 🎰")
    print("""
    RULES:
          
        1. Bet And Win (💎  💀  💲)
        2. The machine will spin and show 3 symbols.
        3. Three same symbols → JACKPOT🤑 : Your money is 2X
        4. Two same symbols → DOUBLED✌️ : Your money is back
        5. All different symbols → BUSTED💥 : Your money is lost

    Good luck! 😈
    """
    )
    input("PRESS ENTER TO PLAY.....")

def deposit():
    while True:
        clear()
        balance =input ("How much you like to deposit ($" + str(MIN_DEPOSIT) + " - $" + str(MAX_DEPOSIT) + " ): $")

        if balance.isdigit():
            if MIN_DEPOSIT <= int(balance) <= MAX_DEPOSIT:
                break
            else:
                print("Invalid...")
                input("press ENTER to continue")
        else:
            print("Invalid...")
            input("press ENTER to continue")
    return int(balance)


def bet (balance):
    while True:
        clear()
        print(f"You have: ${balance}")
        bet_amt = input ("How much you like to bet (mini: $" + str(MIN_BET) + "): $")

        if bet_amt.isdigit():
            if MIN_BET <= int(bet_amt) <= balance:
                break
            else:
                if int(bet_amt)< MIN_BET:
                    print("Bet at least $10.")
                    input("press ENTER to continue")
                if int(bet_amt)> balance:
                    print("Insufficient Balance.")
                    input("press ENTER to continue")
        else:
            print("Invalid...")
            input("press ENTER to continue")
    return int(bet_amt)

def check_result (line, bet ):

    global balance

    max_sym = max(line, key=line.count)
    count = line.count(max_sym)
        
    if count == 1:
        print("\nBUSTED💥, Opps! You losse Your bet 😢")
        balance -= bet
        print(f"Current balance: ${balance}")

    elif count == 2:
        print("\nDOUBLED✌️, Thank god! You got your money back 😇")
        print(f"Current balance: ${balance}")

    elif count == 3:
        print("\nJACKPOT 🤑, Lucky! You Win 2x 🎉")
        balance +=2*bet
        print(f"Current balance: ${balance}")
    else :
        print("error occrurs in check_result func")
        exit()

def main():
    global balance
    wlc_screen()
    balance = deposit()
    while True:
        
        bet_amt = bet(balance)
        line = spin_slot_machine()

        print(f"Your Bet: ${bet_amt}")
        check_result(line,bet_amt)

        
        ch = input("\nWanna Bet Again?? (y/n): ").lower()
        if ch != "y":
            main()
        elif balance < 10:
            print("\nInsufficient balance!!")
            ch = input("\nDo you wants to Deposit Again ? (y/n): ").lower()
            if ch == "y":
                balance = deposit()
            else:
                main()
        else:
            continue
    
main()