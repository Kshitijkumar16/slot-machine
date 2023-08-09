import random

MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1


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
     while True:
          amount = input("\nHow many chips would you like to deposit?\n\t")
          if amount.isdigit():
               amount = int(amount)
               if amount > 0:
                    break
               else:
                    print("\nAmount you deposit must be more than 0/-")
          else:
               print("\nPlease enter a number!!")
     return amount

def ask_nof_lines():
     while True:
          lines = input("How many lines you want to bet on? (1 - " + str(MAX_LINES) + ") \n\t")
          if lines.isdigit():
               lines = int(lines)
               if 0 < lines <= MAX_LINES:
                    break
               else:
                    print("\nPlease enter a valid number of lines to bet on.")
          else:
               print("\nPlease enter a number!!")
     return lines

def ask_bet():
     while True:
          bet = input("How much would you like to bet per line? \n\t")
          if bet.isdigit():
               bet = int(bet)
               if bet > MAX_BET:
                    print("\nYou cannot bet for more than the maximum amount of chips set per instructions. (1000 chips)")
               elif bet < 1:
                    print("You must at least bet for 1 chip.")
               else:
                    break
          else:
               print("\nPlease enter a number!!")
     return bet



# Main body of the program 
def main():
     instruct = instructions()
     balance = deposit()
     lines = ask_nof_lines()
     
     while True:
          bet = ask_bet()
          total_bet = bet * lines
          
          if total_bet > balance:
               print("\t! You haven't deposited enough chips to make this bet ! ")
          else:
               break
               
     print(f"\nYou are betting {bet} chips on {lines} lines. Total bet is {total_bet} chips.\n")

main()