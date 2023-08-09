# Importing modules
import random

# Defining global constants
MAX_LINES = 3             # Maximum number of lines in the slot machine
MAX_BET = 1000            # Maximum bet on a line
MIN_BET = 1               # Minimum bet on a line

ROWS = 3                  # Rows in the slot machine display
COLS = 3                  # Columns in the display

# Dictionary containing all symbols in a single column/reel
symbol_count_perCol = {
     "A" : 1,             # 1 A on a column reel
     "B" : 2,               
     "C" : 3,
     "D" : 4,             # 4 D's on the column reel
}

# Function to display all the instructions to the user
def instructions():
     print("\n\n**********************************************************************************************************\n")
     print("\t\t\t\t!!  GRAND CASINO SLOT MACHINE  !!\n")
     print("Rules - \n\t1. You first have to deposite an amount of chips upto 3000 max.\n\t2. You can bet on 1 - 3 lines at a time.")
     print(f"\t3. You cannot bet more than {MAX_BET} chips and less than {MIN_BET} chip per line.")
     print("\t4. The slot machine looks like this -\n\t\t A | D | B \t<-- line 1\n\t\t C | C | C \t<-- line 2  (a WIN on a line looks like this)\n\t\t D | A | C \t<-- line 3")
     print("\t5. Betting on 1 line means TOP line, betting on two lines means TOP TWO lines.")
     print("\nGood luck!\n")
     print("**********************************************************************************************************\n")
     print("\nHi! This is Venessa!")

# Function to take deposit from user
def deposit():
     while True:                                 # To continuously ask user for input until its correct
          amount = input("\nHow many chips would you like to deposit?\n\t")
          if amount.isdigit():                   # To make sure its a positive integer 
               amount = int(amount)
               if amount > 0:                    # Doing zero check
                    break
               else:
                    print("\nAmount you deposit must be more than 0/-")
          else:
               print("\nPlease enter a number!!")
     return amount

# Function to ask user how many lines they want to bet on
def ask_nof_lines():
     while True:
          lines = input("How many lines you want to bet on? (1 - " + str(MAX_LINES) + ") \n\t")
          if lines.isdigit():
               lines = int(lines)
               if 0 < lines <= MAX_LINES:        # Validating users chosen number of lines
                    break
               else:
                    print("\nPlease enter a valid number of lines to bet on.")
          else:
               print("\nPlease enter a number!!")
     return lines

# Function to ask for the bet price 
def ask_bet():
     while True:
          bet = input("How much would you like to bet per line? \n\t")
          if bet.isdigit():
               bet = int(bet)
               if bet > MAX_BET:                 # Validating the bet price
                    print("\nYou cannot bet for more than the maximum amount of chips set per instructions. (1000 chips)")
               elif bet < 1:
                    print("You must at least bet for 1 chip.")
               else:
                    break
          else:
               print("\nPlease enter a number!!")
     return bet

# Function to generate the columns
def spin_the_slots(rows, cols, symbols):
     # Generating a list containing all the possible symbols with accurate count
     all_symb  = []
     for sym, sym_c in symbols.items():
          for _ in range(sym_c):
               all_symb.append(sym)       # Adding each symbol with their occurance int he list
     
     # for _ in all_symb:
     #      print(_, end=", ")
     
     columns = []
     for _ in range(COLS):
          column = []
          current_symb = all_symb[:]      # Making a copy of the list so we dont change the original list
          for _ in range(ROWS):
               value = random.choice(current_symb)
               column.append(value)       # Adding the chosen symbol to the column 
               current_symb.remove(value) # Removing the chosen symbol from the list, so we dont choose it again
          columns.append(column)     
          
     return columns

# Function to display the slot machine after spinning    
def display_slots(columns): 
     print()
     # We need to print transpose of this matrix which we got after spinning function 
     for row in range(len(columns[0])):
          for i, column in enumerate(columns):   # Getting index as well to know when to print the next line
               if i == len(columns) - 1:
                    print(column[row], end="")
               else:
                    print(column[row], end=" | ")
          print()
          


# ___________________________________________Main body of the program _____________________________________________________________

def main():
     # 1. Taking the bet
     instructions()
     # balance = deposit()
     # lines = ask_nof_lines()
     
     # # This while loop keeps the total bet price less than or equal to the deposited amount
     # while True:                         
     #      bet = ask_bet()
     #      total_bet = bet * lines
          
     #      if total_bet > balance:
     #           print("\t! You haven't deposited enough chips to make this bet ! ")
     #      else:
     #           break
     
     # # Informing user mid process          
     # print(f"\nYou are betting {bet} chips on {lines} lines. Total bet is {total_bet} chips.\n")

     # 2. Processing the bet
     spinned_slots = spin_the_slots(ROWS, COLS, symbol_count_perCol)
     displayed_slots = display_slots(spinned_slots)
     
main()