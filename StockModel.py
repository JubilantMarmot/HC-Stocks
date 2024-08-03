class StockModel:
    def __init__(self, tckr):

        try:

            self.Ticker = tckr['01. symbol']
            self.OpeningPrice = tckr['02. open']
            self.dayHigh = tckr['03. high']
            self.dayLow = tckr['04. low']
            self.Last_Price = tckr['05. price']
            self.volume = tckr['06. volume']

            # For now:
            self.fifty2weeksHigh = tckr['03. high']
            self.fifty2weeksLow = tckr['04. low']

            self.change_day = tckr['09. change']
            self.change_per_day = tckr['10. change percent']

        except RuntimeError:
            print("Error in parsing ticker", self.Ticker, ". Skipping")


    '''
    
    01. symbol:"MSFT"
    02. open:"151.6500"
    03. high:"153.4200"
    04. low:"151.0200"
    05. price:"152.0600"
    06. volume:"9425575"
    07. latest trading day:"2019-12-12"
    08. previous close:"151.7000"
    09. change:"0.3600"
    10. change percent:"0.2373%"
    '''

    def printStockModel(self):
        print('Stock info as follows:')
        print('Ticker :', self.Ticker)
        print('Last_Price :', self.Last_Price)
        print('OpeningPrice :',  self.OpeningPrice)
        print('fifty2weeksLow :', self.fifty2weeksLow)
        print('fifty2weeksHigh :', self.fifty2weeksHigh)
        print('dayLow :', self.dayLow)
        print('dayHigh :', self.dayHigh)
