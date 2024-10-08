# Creating a slot machine where a user can deposit money to place a bet.
# deposit money, place bet, determine if they won, keep playing until they cash out or lose all money
# collect money, add to balance, allow them to bet on line, spin machine, did they win on the line?, generate items in reels, add winnings to balance

#generate random spins - if you get 3 in a row you win
import random

#add a global constant to us in any function when called (caps as its constant)
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 2

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines            

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)  

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="") 

        print()               

#create a function to collect user input. Checking if input is a digit we need to check if the number is greater than 0 which we can convert into an int. If input is not a digit we wil ask to input a digit. 
def deposit():
    while True:
        amount = input("What amount would you like to deposit? £")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount  

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number.")

    return lines  

def get_bet():
    while True:
        amount = input("What amount would you like to bet? £")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount  

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You dont have enough to bet that amount, your current balance is: £{balance}")
        else:
            break        
    print(f"You are betting £{bet} on {lines} lines. Total bet is equal to: £{total_bet}")


    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won £{winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

#Calling the actual programme main - this is where the game begins
def main():
    balance = deposit()
    while True:
        print(f"Current balance is: £{balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with £{balance}")    
   


main()


