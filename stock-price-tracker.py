import pandas as pd
import pandas_datareader as pdr
from time import sleep

#creates list of symbols and splits each value into individual symbol
test_symbols = "AMZN GOOG NFLX FB GLD SPY".split()

#personal stock portfolio (from Dec 2020) of stocks projected to grow between years 2020-2030
tech_symbols = "WUGI CEVA FIVG INSG AMD VUZI TSLA THNQ DT DLR BOTZ NIO INTC NVDA".split()
www_symbols = "BIDU GOOG GOOGL".split()
energy_symbols = "ALB ENPH SEDG BEP".split()

options = " Track Default List, Show Default List, \
Add to Default, Edit Default List, Add new List, \
        Quit".split(",")
        
def show_default(test_symbols): #2
    test_symbols.sort()
    return test_symbols

def add_to_default(test_symbols): #3
    print("Enter symbol to add: ")
    symbol = input().upper() #convert input to uppercase
    while symbol != '':
        test_symbols.append(symbol)
        symbol = input("Hit enter at anytime to quit program.\nEnter symbol to add:") #hook
    
def edit_default(test_symbols): #4
    print("Select symbol to delete: ")
    #select from menu of symbols
    for i in range(1, len(test_symbols) + 1):
        print("{} - {}".format(i, test_symbols[i-1]))
    remove = test_symbols.pop(int(input())-1)
    print("{} removed".format(remove))

def add_list(): #5
    new_list = []
    print("Enter symbol to add: ")
    symbol = input().upper()
    while symbol != '':
        new_list.append(symbol)
        symbol = input("Hit enter at anytime to quit program.\nEnter symbol to add:")
    while True:
        print(get_prices(new_list))
        print("CNTL + C to quit")

#define function called get_prices which takes argument as split objects in list "symbols" and returns price
def get_prices(test_symbols):
    test_symbols.sort() #sorts in alphabetical order
    return pdr.get_quote_yahoo(test_symbols)['price'] #function returns ONLY prices of live stock quotes for each ticker symbol

def get_prices(tech_symbols):
    tech_symbols.sort() 
    return pdr.get_quote_yahoo(tech_symbols)['price']

def get_prices(www_symbols):
    www_symbols.sort() 
    return pdr.get_quote_yahoo(www_symbols)['price']

def get_prices(energy_symbols):
    energy_symbols.sort()
    return pdr.get_quote_yahoo(energy_symbols)['price']

#define entry point for application
def main():
    run_program = True #hook feature to later change to False for Quit menu option
    while run_program: #infinite loop
        print("\nChoose Option:") #menu heading
        for i in range(1, len(options) + 1):
            print("{} - {}".format(i, options[i-1]))
        #create checkpoint so not constantly running
        choice = int(input()) #user input integer
        
        #make a structure to implement certain code when a choice is made
        if choice == 1:
            while True: #implements counter
                print("\n-Test- General stocks")
                print(get_prices(test_symbols)) #prints prices of symbols
        
                print("\nTech stocks")
                print(get_prices(tech_symbols))
        
                print("\nWWW stocks")
                print(get_prices(www_symbols))
            
                print("\nEnergy stocks")
                print(get_prices(energy_symbols))
        
                print("\nCNTL + C to quit") #instructions for user to exit loop
                sleep(5) #5 second refresh counter    
        
        elif choice == 2:
            print(show_default(test_symbols))
        elif choice == 3:
            add_to_default(test_symbols)            
        elif choice == 4:
            edit_default(test_symbols)     
        elif choice == 5:
            add_list()            
        elif choice == 6:
            run_program = False #Quit
        
if __name__ == "__main__": #run upon initialization
    main()
