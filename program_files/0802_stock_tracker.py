import sys
import pandas_datareader as pdr
from time import sleep, time
import os




def display_menu():
    print(
        """
        StockTracker Menu
        1. Track watchlist
        2. Add watchlist
        3. Edit watchlist
        4. Delete watchlist
        5. Exit
        """
    )

def track():
    show_lists()
    start = time()
    symbols = 'AMZN NFLX GOOG FB'.split()
    while True:
        print(pdr.get_quote_yahoo(symbols)['price'])
        print(time() - start)
        sleep(1)
        if time() - start >= 10:
            prompt = input("Do you want to continue? ")
            if prompt.lower() == 'n':
                break

def show_lists():
    return watchlists = os.listdir('watchlists')

def add_list():
    pass

def edit_list():
    show_lists()


def delete_list():
    show_lists()


actions = {'1': track, '2': add_list, '3': edit_list, '4': delete_list}

def main():
    # application flow
    if 'watchlists' not in os.listdir():
        os.mkdir('watchlists')
    while True:
        display_menu()
        choice = input('Enter your selection: ')
        if choice in '1234':
            actions[choice]()
        elif choice == '5':
            print("Thanks for using StockTracker!")
            sys.exit()
        else:
            print('Enter a valid choice...')



if __name__ == '__main__':
    main()



