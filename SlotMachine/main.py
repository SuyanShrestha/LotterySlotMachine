import random


MAX_LINES = 3
MAX_BET = 100000
MIN_BET = 500

ROWS = 3
COLS = 3

symbol_count ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
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

        #if no break occurs in for loop
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# 3 same symbols in a row will do the thing
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # Making a copy of all_symbolsz
        current_symbols = all_symbols[:] 
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end =" | ")
            else:
                print(column[row], end = "") # next line

        print()

#Collect the deposit amount 
def deposit():
    while True:
        amount = input("Enter the deposit amount : Rs ")
        if amount.isdigit():
            amount = int(amount)
            if amount >=0:
                break
            else: 
                print("Enter valid amount. Must be greater than zero.")
        else:
            print("Please enter a number.")
    return amount

#How much they wanna bet?
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1 to "+ str(MAX_LINES) + ")? ")
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
        amount = input("How much would you like to bet? : Rs ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else: 
                print(f"Enter valid amount. Must be between {MIN_BET} to {MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        #Check total bet and balance amount 
        if total_bet > balance:
            print(f"Insufficient Balance for the bet Rs {total_bet}. Your current balance is {balance}")
        else:
            break

    print(f"You are betting Rs {bet} on {lines} lines. Your total bet is Rs {total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    print(f"Congratulations! Yo won Rs {winnings}.")
    print(f"You won on lines: ", *winning_lines) # unpack operator
    
    return winnings - total_bet


def main():
    balance = deposit()
    while(True):
        print(f"Your current balance is: Rs {balance}")
        choice = input("Press enter to spin and 'q' to quit.")
        if choice == "q":
            break
        balance += spin(balance)

    print(f"You left with Rs {balance}")
    
main()
