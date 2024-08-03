
from Stock import *
from datetime import datetime, timedelta
from decimal import Decimal
import random

class StockEntry:
    # Stocks entry for the FireBase Database

    def __init__(self, stock, version, ticker):
        self.stock = stock
        self.version = version
        self.TIME_ZONE = "PDT"
        self.Ticker = ticker

        a = 'tmp'
        self.invalidEntry = {
            "buyPrice" :  0.0,
            "confidence" : 0.0,
            "expiryTime" : (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S") + " "+self.TIME_ZONE,
            "pairName" : ticker,
            "sellPrice" : 0.0 ,
            "signalType" : "buy",
            "stopLossVal" : 0.0,
            "triggerTime" : datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " " + self.TIME_ZONE
        }

    def getEntry(self):
        self.ConfidenceVersion  = {"free":82,"light":84,"pro":89,"premium":92,"ultimate":95,"business":98}
        self.confValue = random.randint(self.ConfidenceVersion[self.version]-3, self.ConfidenceVersion[self.version])

        # long vs short
        v = random.randint(0, 1)
        signalTypes = {0:"long",1:"short"}
        self.signalType = signalTypes[v]

        ''' OBSELETE
        print("Stock VLast Price:", float(self.stock.Last_Price))
        self.fifty2weeksRange = (float(self.stock.fifty2weeksHigh) - float(self.stock.fifty2weeksLow))
        self.buyPrice = float(self.stock.Last_Price) - float(self.fifty2weeksRange)*float(0.1)
        self.sellPrice = float(self.stock.Last_Price) + float(self.fifty2weeksRange)*float(0.4)
        self.stopLossVal = float(self.buyPrice) - float(self.fifty2weeksRange)**float(0.3)
        '''

        print("Stock VLast Price:", float(self.stock.Last_Price))
        self.buyPrice = 0.92 * float(self.stock.Last_Price)
        self.sellPrice = 1.12 * float(self.stock.Last_Price)
        self.stopLossVal = 0.93 * self.buyPrice

        self.db_entry = {
            "buyPrice" :  round(self.buyPrice,2),
            "confidence" : self.confValue,
            "expiryTime" : (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S") + " "+self.TIME_ZONE,
            "pairName" : self.stock.Ticker,
            "sellPrice" : round(self.sellPrice,2) ,
            "signalType" : self.signalType,
            "stopLossVal" : round(self.stopLossVal,2),
            "triggerTime" : datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " "+self.TIME_ZONE
        }


        print(self.db_entry)
        if self.buyPrice <= 0 or self.sellPrice <=0 or self.stopLossVal <= 0:
            print('<','='*50,'>')
            print('Invalid entry detected for ', self.Ticker)
            print('<','='*50,'>')
            #self.db_entry = self.invalidEntry

        return self.db_entry






