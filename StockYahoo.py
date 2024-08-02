

from decimal import Decimal
class StockYahoo:


    def __init__(self, str1, ticker):
        #self.Name = fin_data['name']
        keyWords = {}

        try:
            a = 'tmp'
            self.isValidStock = 1

            KEY_KEYWORDS = "keywords"
            KEY_CURRENT_PRICE = "CurrentPrice"
            KEY_REGULAR_MARKET_OPEN = "MarketOpen"
            KEY_FIFTY_TWO_WK_RANGE_VALUE = "FIFTY_TWO_WK_RANGE-value"
            KEY_DAYSRANGEVALUE = "DAYS_RANGE-value"

            # Contains location for each string
            keyWords[KEY_KEYWORDS] = str1.find(KEY_KEYWORDS)
            keyWords[KEY_CURRENT_PRICE] = str1.find("data-symbol=\""+ticker+"\" data-test=\"qsp-price\" data-field=\"regularMarketPrice\" data-trend=\"none\" data-pricehint")
            keyWords[KEY_REGULAR_MARKET_OPEN] = str1.find("<td class=\"Ta(end) Fw(600) Lh(14px)\" data-test=\"OPEN-value\"")
            keyWords[KEY_FIFTY_TWO_WK_RANGE_VALUE] = str1.find(KEY_FIFTY_TWO_WK_RANGE_VALUE)
            keyWords[KEY_DAYSRANGEVALUE] = str1.find(KEY_DAYSRANGEVALUE)

            text_file = open("sample.txt", "w")
            n = text_file.write('Welcome to pythonexamples.org')
            text_file.write(str1)
            text_file.close()


            print(keyWords)
            if -1 in keyWords.values():
                print("One or more of the Keywords are not found (anything with -1). Exiting.")
                print(keyWords)

                #exit(1)

            #keywords
            loc = keyWords[KEY_KEYWORDS]
            self.Name = (str1[loc:loc+50]).split("=")[1].split(',')[1]

            #regularMarketPrice
            loc = keyWords[KEY_CURRENT_PRICE]
            self.Last_Price = str1[loc:loc+150].split("active=\"\">")[1].split("<")[0]
            print("Last known price -> ", self.Last_Price)

            #regularMarketOpen
            #loc = str1.find("<td class=\"Ta(end) Fw(600) Lh(14px)\" data-test=\"OPEN-value\"")
            print(str1[loc:loc+200].split("active=\"\">")[1].split("<")[0])
            self.OpeningPrice = str1[loc:loc+200].split("active=\"\">")[1].split("<")[0]
            print("Open price -> ", self.OpeningPrice)
            #FIFTY_TWO_WK_RANGE
            loc = keyWords[KEY_FIFTY_TWO_WK_RANGE_VALUE]
            [self.fifty2weeksLow, self.fifty2weeksHigh] = (str1[loc:loc+80]).split(">")[1].split('<')[0].split('-')
            print("fifty2weeksLow -> ", self.fifty2weeksLow)
            print("fifty2weeksHigh -> ", self.fifty2weeksHigh)
            #DAYS_RANGE
            loc = keyWords[KEY_DAYSRANGEVALUE]
            [self.dayLow, self.dayHigh] = (str1[loc:loc+80]).split(">")[1].split('<')[0].split('-')

            self.Ticker = ticker
            self.dayLow = self.dayLow.replace(',','').strip()
            self.dayHigh = self.dayHigh.replace(',','').strip()
            self.fifty2weeksHigh = self.fifty2weeksHigh.replace(',','').strip()
            self.Last_Price = self.Last_Price.replace(',','').strip()
            self.OpeningPrice = self.OpeningPrice.replace(',','').strip()
            self.fifty2weeksLow = self.fifty2weeksLow.replace(',','').strip(',')

            print(self.fifty2weeksLow)
            print(self.fifty2weeksHigh)

            self.Last_Price = float(self.Last_Price)
            self.OpeningPrice = float(self.OpeningPrice)
            self.fifty2weeksLow = float(self.fifty2weeksLow)
            self.fifty2weeksHigh = float(self.fifty2weeksHigh)
            self.dayLow = float(self.dayLow)
            self.dayHigh = float(self.dayHigh)


            self.printStockYahoo()
        except RuntimeError:
            print("Error in parsing ticker", self.Ticker, ". Skipping")



    def printStockYahoo(self):
        print('Stock info as follows:',self.Ticker,'(',self.Ticker,'):')
        print('Real time price:(',self.Last_Price,')')
        print('Open Price:(',self.OpeningPrice,'). Low: (',self.dayLow,'). High: (',self.dayHigh,').')
        print('52 weeks Low:(',self.fifty2weeksLow,'). 52 weeks high: (',self.fifty2weeksHigh,').')
        #print('Volume:(',self.volume,'). EPS: (',self.EPS,'). Price Earning Ratio: ', self.Price_Earnings_Ratio,').')

    '''
    self.Ticker
    self.Last_Price
    self.OpeningPrice
    self.fifty2weeksLow
    self.fifty2weeksHigh
    self.dayLow
    self.dayHigh
    '''