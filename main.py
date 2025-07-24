import random 
from colorama import init, Fore, Style
init(autoreset=True)

def display_board(board):
    print()
    def colored(cell):
        if cell == 'X':
            return Fore.RED +cell + Style.RESET_ALL
        elif cell=='0':
            return Fore.BLUE +cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell +Style.RESET_ALL
    print(''+ colored(board[0]) + '|' + colored(board[1])+ '|'+ colored(board[2]))
    print(Fore.CYAN + '_______________'+ Style.RESET_ALL)
    print('' +colored(board[4])+ '|' +colored(board[3])+ '|'+colored(board[5]))
    print(Fore.CYAN+ '________________' + Style.RESET_ALL)
    pritn('' + colored(board[6])+'|' + colored(board[7])+ '|' +colored(board[8]))
    print()

def player_choice():
    symbol=''
    while symbol not in ['X', 'O']:            
        symbol = input(Fore.GREEN + "do you want to be X or O"+Style.RESET_ALL).upper()
