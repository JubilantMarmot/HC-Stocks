
#from googlefinance.client import get_price_data, get_prices_data, get_prices_time_data
import json
import requests
from Stock import *
from StockEntry import *
from Util import *
import random, time
from datetime import datetime, timedelta
import pandas as pd

class GoStocks:
    def __init__(self):
        self.Util = Util()
        self.symbols = None
        self.VERSIONS = {0:"free",1:"light",2:"pro",3:"premium",4:"ultimate",5:"business"}
        self.TCIKERS_FILE_NAME = "tickers/signals_tickers.json"

        self.S0 = "s0"
        self.S1 = "s1"
        self.S2 = "s2"
        self.S3 = "s3"
        self.S4 = "s4"
        self.S5 = "s5"

        self.stcks = self.loadTickers()


        self.POOL__STOCKS = [random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks),
                             random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks),
                             random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks),
                             random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks),
                             random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks),
                             random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks), random.choice(self.stcks)]


        self.list_stocks = {self.VERSIONS[0]:self.POOL__STOCKS[0:4],
                            self.VERSIONS[1]:self.POOL__STOCKS[4:8],
                            self.VERSIONS[2]:self.POOL__STOCKS[8:12],
                            self.VERSIONS[3]:self.POOL__STOCKS[12:16],
                            self.VERSIONS[4]:self.POOL__STOCKS[16:20],
                            self.VERSIONS[5]:self.POOL__STOCKS[20:24]}


        self.out_json = {self.VERSIONS[0]:{"s0":{},"s1":{},"s2":{},"s3":{}},
                         self.VERSIONS[1]:{"s0":{},"s1":{},"s2":{},"s3":{}},
                         self.VERSIONS[2]:{"s0":{},"s1":{},"s2":{},"s3":{}},
                         self.VERSIONS[3]:{"s0":{},"s1":{},"s2":{},"s3":{}},
                         self.VERSIONS[4]:{"s0":{},"s1":{},"s2":{},"s3":{}},
                         self.VERSIONS[5]:{"s0":{},"s1":{},"s2":{},"s3":{}}}

    def add_all_db_entries(self, version, db_entries):
        print("->"*5, version)
        print("->"*5, db_entries)

        self.out_json[version] = {self.S3:db_entries.pop(),self.S2:db_entries.pop(),self.S1:db_entries.pop(),self.S0:db_entries.pop()}

    def get_rnd_stck(self):
        return random.choice(self.stcks)

    def loadTickers(self):
        # Opening JSON file
        f = open(self.TCIKERS_FILE_NAME)
        all_tickers = json.load(f)
        print(all_tickers["tickers"])
        return all_tickers["tickers"]



    def prepareStocks(self):

        print("The following has been assigned")
        for v in self.list_stocks.keys():
            print(v, " -> ", self.list_stocks[v])

        for version in self.list_stocks.keys():
            print("*"*50)
            print('Version -> ', version)
            list_stocks = self.list_stocks[version]
            db_entries = []
            print("->"*30)
            for ticker in list_stocks:

                print("Version: ", version, " -> Ticker: ", ticker)

                stock = self.Util.gStockAPI(ticker)

                if stock == None:
                    print('<','='*50,'>'),
                    print('Invalid ticker', ticker)
                    break
                    db_entries.append(s_entry.invalidEntry)
                else:
                    s_entry = StockEntry(stock, version, ticker)
                    print(stock.printStockModel())
                    db_entries.append(s_entry.getEntry())

            self.add_all_db_entries(version, db_entries)
            print(self.out_json)

### Requet Dat from API and prepare as Json
goStocks = GoStocks()
goStocks.prepareStocks()

import json
from datetime import datetime
json = json.dumps(goStocks.out_json)
fileName = "signals/stocks.json"+str(datetime.now())[:10]+".json"
f = open(fileName,"w")
f.write(json)
f.close()
print(goStocks.out_json)
print('********************* JASON file is READY TO UPLOAD: Stored at: ********************* ')
print(fileName)
print('************************************************************************************ ')

######################################

