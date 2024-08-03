import time, requests, json
from StockModel import *

class Util:

    def __init__(self):
        self.className = "StocksAPI"

    def gStockAPI(self, ticker):

        # Rate limit 8 per minute.
        time.sleep(15)

        url = "https://alpha-vantage.p.rapidapi.com/query"
        querystring = {"function":"GLOBAL_QUOTE","symbol":ticker,"datatype":"json"}
        headers = {
            "X-RapidAPI-Key": "<removed api key>",
            "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
        }

        rsp = requests.get(url, headers=headers, params=querystring)

        if rsp.status_code in (200,):
            print(rsp.json())
            tkr = rsp.json()["Global Quote"]
            print(tkr['01. symbol'])
            return StockModel(tkr)
        return None
