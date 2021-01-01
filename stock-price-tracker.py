import pandas as pd
import pandas_datareader as pdr
from time import sleep

#create list of symbols and split each value into individual symbol
symbols = "AMZN GOOG NFLX FB GLD SPY".split()

#author's personal stock portfolio (compiled Dec 2020) of stocks projected to grow between years 2020-2030
tech_symbols = "WUGI CEVA FIVG INSG AMD VUZI TSLA THNQ DT DLR BOTZ NIO NVDA".split()
www_symbols = "BIDU GOOG GOOGL".split()
energy_symbols = "ALB ENPH SEDG BEP".split()

options = " Track all Lists, Show all Lists, \
Add to Default List, Edit Default List, Search live price of any stock:, \
        Quit".split(",")

#define function called get_prices to take arguments as the split objects from list "symbols" and returns each object's price only
def get_prices(symbols): #choice 1
    symbols.sort() #sort in alphabetical order
    return pdr.get_quote_yahoo(symbols)['price'] 
        
def show_default(symbols): #choice 2
    symbols.sort() 
    return symbols

def add_to_default(symbols): #choice 3
    print("Enter symbol to add: ")
    symbol = input().upper() #convert input to uppercase
    while symbol != '':
        symbols.append(symbol)
        symbol = input("Hit enter at anytime to quit program.\nEnter symbol to add:") #hook
    
def edit_default(symbols): #choice 4
    print("Select symbol to delete: ")
    #select from menu of symbols
    for i in range(1, len(symbols) + 1):
        print("{} - {}".format(i, symbols[i-1]))
    remove = symbols.pop(int(input())-1)
    print("{} removed".format(remove))

def stock_search(): #choice 5
    new_list = []
    print("Enter ticker symbol to search: ")
    symbol = input().upper()
    while symbol != '':
        new_list.append(symbol)
        symbol = input("Hit enter again to track live stock price.")
    while True:
        print(get_prices(new_list))
        print("CNTL + C to quit")

#define entry point for application
def main():
    run_program = True
    while run_program: #infinite loop
        print("\nChoose Option:") #menu heading
        for i in range(1, len(options) + 1):
            print("{} - {}".format(i, options[i-1]))
        #create checkpoint so loop not constantly running
        choice = int(input()) #user input integer
        
        #make a structure to implement certain code when a choice is made
        if choice == 1:
            while True: #implements counter
                print("\nDefault stocks (customizable)")
                print(get_prices(symbols)) #prints prices of symbols

                print("\nTech stocks")
                print(get_prices(tech_symbols))
        
                print("\nWWW stocks")
                print(get_prices(www_symbols))
            
                print("\nEnergy stocks")
                print(get_prices(energy_symbols))
        
                print("\nCNTL + C to quit") #instructions for user to exit loop
                sleep(5) #5 second refresh counter    
        
        elif choice == 2:
            print("\nDefault stocks (customizable): ",show_default(symbols))
            print("\nTech sector: ", show_default(tech_symbols))
            print("\nWWW sector: ",show_default(www_symbols))
            print("\nEnergy sector: ", show_default(energy_symbols))
            
        elif choice == 3:
            add_to_default(symbols)            
        elif choice == 4:
            edit_default(symbols)     
        elif choice == 5:
            stock_search()           
        elif choice == 6:
            run_program = False #Quit
        
if __name__ == "__main__": #run upon initialization
    main()
