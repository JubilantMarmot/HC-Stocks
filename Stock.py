from decimal import Decimal

class Stock:


    def __init__(self):
        a = 'tmp'
        self.isValidStock = 1

    def getStock(self,fin_data):
        self.OpeningPrice = fin_data['op']
        self.Price_Earnings_Ratio = fin_data['pe']
        self.fifty2weeksHigh = fin_data['hi52']
        self.fifty2weeksLow = fin_data['lo52']
        self.Ticker = fin_data['t']
        self.Exchange_Name = fin_data['e']
        self.Last_Price = fin_data['l']
        self.dayLow = fin_data['lo']
        self.dayHigh = fin_data['hi']
        self.volume = fin_data['vo']
        self.EPS = fin_data['eps']
        self.dividends = fin_data['ldiv']
        self.shares = fin_data['shares']
        self.market_cap = fin_data['mc']
        self.Name = fin_data['name']

        return self


    def printStock(self):
        print('Stock info as follows:',self.Name,'(',self.Ticker,'):')
        print('Real time price:(',self.Last_Price,')')
        print('Open Price:(',self.OpeningPrice,'). Low: (',self.dayLow,'). High: (',self.dayHigh,').')
        print('52 weeks Low:(',self.fifty2weeksLow,'). 52 weeks high: (',self.fifty2weeksHigh,').')
        print('Volume:(',self.volume,'). EPS: (',self.EPS,'). Price Earning Ratio: ', self.Price_Earnings_Ratio,').')
        print('Dividends:(',self.dividends,'). Shares: (',self.shares,'). Market Cap: ', self.market_cap,').')

    def isValid(self, fin_data):
        k = fin_data.keys()
        vs = ['op', 'pe','hi52','lo52','t','e','l','lo','hi','vo','eps','ldiv','shares','mc','name']
        for v in vs:
            if v not in k:
                self.isValidStock = 0
                return 0

        self.isValidStock = 1
        return 1
