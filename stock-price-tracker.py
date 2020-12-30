import pandas as pd
import pandas_datareader as pdr
from time import sleep

#creates list of symbols and splits each value into individual symbol
test_symbols = "AMZN GOOG NFLX FB GLD SPY".split()

#personal stock portfolio (from Dec 2020) of stocks projected to grow between years 2020-2030
tech_symbols = "WUGI CEVA FIVG INSG AMD VUZI TSLA THNQ DT DLR BOTZ NIO INTC NVDA".split()
www_symbols = "BIDU GOOG GOOGL".split()
energy_symbols = "ALB ENPH SEDG BEP".split()

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
    while True: #infinite loop
        print("\nGeneral (test) stocks")
        print(get_prices(test_symbols)) #prints prices of symbols
        
        print("\nTech stocks")
        print(get_prices(tech_symbols))
        
        print("\nWWW stocks")
        print(get_prices(www_symbols))
        
        print("\nEnergy stocks")
        print(get_prices(energy_symbols))
        
        print("\nCNTL + C to quit") #instructions for user to exit loop
        sleep(10) #sleep for 10 seconds to refresh list of quotes
        
if __name__ == "__main__": #run upon initialization
    main()