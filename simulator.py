import pandas as pd
import time
from colored import stylize, Fore, Style, fore

class Simulator:

    def __init__(self):
        print("Initiated")
        # TODO: Add restore for csv at the end so you can loop
        
    def get_csv_size(self):
        x = pd.read_csv('csv/Nick C.csv')
        return len(x)
    
    def consume(self):
       x =  pd.read_csv("csv/Nick C.csv")
       row_to_consume = x.head(1)
       print(row_to_consume)
       x = x.drop(index=0)
       print(x.head())
       print(f'\n{Style.bold}{Fore.green}Stored row \n{Style.reset}')
       self.postRow(row_to_consume)
       x.to_csv("csv/Nick C.csv", index=False)
       self.get_csv_size()

    def wait(self, duration):
        print("Waiting for " + str(duration) + " seconds")
        time.sleep(duration)
    
    def driver(self):
        while(self.get_csv_size() > 0):
            self.consume()
            print(self.get_csv_size())
            self.wait(.1)
        print(stylize('Consumed', fore('blue')))
        
    def postRow(self, row):
        print(f'{Fore.yellow}{Style.bold}📡📶 Sending row to REST \n {Style.reset}' + str(row))

# Driver
s = Simulator()
s.driver()

