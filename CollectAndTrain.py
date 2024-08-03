from GoStocks import *
import pandas as pd
from Util import *
import os
import csv
import time

class CollectAndTrain:
    def __init__(self):
        self.className = "collectAndTrain"

        '''
        self.POOL__STOCKS = {"FB","CEVA","TWTR","BK",
                             "PBI","C","FB","AAPL",
                             "HBI", "COT","AXP","CHGG",
                             "TD","VSLR","B","BOX",
                             "MOBL","GE","FB","TD"}
        '''



        self.fv_all = pd.DataFrame()
        self.util = Util()

        now = datetime.now()
        self.TodayDate = "{0}-{1}-{2}".format(now.year,now.month,now.day)

        self.partition_size = 300 # partition of tickers

    def setTickers(self, file):
        tickers = pd.read_csv(file, delimiter=',', header=0)
        Composite = tickers["Symbol"].tolist()



        self.all_tickers = Composite
        print(self.all_tickers)

    def write_data(self, df, block):
        if df is None:
            return
        dirName = 'features'
        if not os.path.exists(dirName):
            os.makedirs(dirName)
        os.chdir(dirName)

        today = self.TodayDate
        file = today+'_'+str(block)+'.parquet'

        df.to_parquet(file,engine='auto', compression='GZIP')

        os.chdir("..")
        return

    def collectDataByPartitions(self):

        start_partition = 0

        finished = False
        block = 0
        failedTickers = []
        while not finished:

            end_partition = start_partition + self.partition_size
            if end_partition > len(self.all_tickers):
                end_partition = len(self.all_tickers)

            tickers_partition = self.all_tickers[start_partition: end_partition]

            [fv_partition, failedTickers] = self.collectData(tickers_partition, failedTickers)
            print(fv_partition)
            self.write_data(fv_partition, block)
            block +=1
            start_partition += end_partition
            print("FAILED:", failedTickers)
            print("Sleeping for 4 minutes:", failedTickers)

            time.sleep(480)
        return

    def collectData(self, tickers_partition, failedTickers):

        fv_partition = None
        for ticker in tickers_partition:
            print('Working on', ticker, ' ... ticker ..')
            try:
                stock = self.util.gStock(ticker.replace(".","").strip())
                if stock.isValidStock == 1:
                    fv = self.computeFeatureVector(stock)
                else:
                    print('Failed', ticker)
                    failedTickers.append(ticker)
                    continue

                if fv_partition is None:
                    fv_partition = fv
                else:
                    fv_partition = fv_partition.append(fv)
            except Exception:
                failedTickers.append(ticker)
                print('Failed', ticker)

        return [fv_partition, failedTickers]

    def computeFeatureVector(self, stock):
        fv = pd.DataFrame()
        d = {'col1': [1, 2], 'col2': [3, 4]}
        fv["OpeningPrice"] = [stock.OpeningPrice]
        fv["Price_Earnings_Ratio"] = [stock.Price_Earnings_Ratio]
        fv["fifty2weeksHigh"] = [stock.fifty2weeksHigh]
        fv["fifty2weeksLow"] = [stock.fifty2weeksLow]
        fv["Ticker"] = [stock.Ticker]
        fv["Exchange_Name"] = [stock.Exchange_Name]
        fv["Last_Price"] = [stock.Last_Price]
        fv["dayLow"] =  [stock.dayLow]
        fv["dayHigh"] = [stock.dayHigh]
        fv["volume"] = [stock.volume]
        fv["EPS"] = [stock.EPS]
        fv["dividends"] = [stock.dividends]
        fv["shares"] = [stock.shares]
        fv["market_cap"] = [stock.market_cap]
        fv["Name"] = [stock.Name]
        fv["quotedate"] = [self.TodayDate]
        return fv

### Collecting the data for Storing
start = datetime.now()
features = CollectAndTrain()

print("**************** Nasdaq *************")
# All symbols for Nasdaq and NYSE
#features.setTickers('tickers/Nasdaq.csv')
#features.collectDataByPartitions()
#print("**************** Nasdaq took {0} *************".format(datetime.now()-start))
print("**************** NYSE *************")
start = datetime.now()
features.setTickers('tickers/NYSE.csv')
features.collectDataByPartitions()
print("**************** NYSE took {0} ****************".format(datetime.now()-start))

######################


