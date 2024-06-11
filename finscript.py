import asyncio
from requests_html import AsyncHTMLSession
import pandas as pd

class Tickers:
    def __init__(self,ticker,url,table,epsilon,actual):
        self.data = []
        self.YTD_rows = []
        self.url = url
        self.table = table
        self.ticker = ticker
        self.epsilon = epsilon
        self.actual = actual

    async def scrape_vanguard_data(self):
        asession = AsyncHTMLSession()

        response = await asession.get(self.url)
        await response.html.arender(timeout=20)

        dist_table = response.html.find(self.table, first=True)
        if dist_table:
            rows = dist_table.find("tr")
            for i in range(len(rows)):
                self.data.append(rows[i].text)
        else:
            print("Table not found")

        await asession.close() 

    def split_row_elem(self,elem):
        split_elem = elem.splitlines()
        return split_elem

    def parse_arr(self):
        parsed = []
        for elem in self.data:
            parsed.append(self.split_row_elem(elem))
        return parsed

    def sum_ppshare(self):
        sum_ = 0
        processed = self.parse_arr()
        processed.pop(0)
        for col in processed:
            if col[3][9] == '4':
                self.YTD_rows.append(col)
                sum_ += float(col[1][1:])
        return sum_

    def f_total(self):
        sum_ = self.sum_ppshare()
        start = 9.66
        end = 9.42
        total = ((sum_ + end) - start) / start 
        return round(total * 100,2)

    def assert_(self,f_t):
        if abs(f_t - self.actual) < self.epsilon: 
            print("\nTicker: " + self.ticker + "\nf_total(YTD): " + str(f_t) + "\nTest passed within margin of error (" + str(epsilon) + ")\n")
        else:
            print("\nTest failed or was outside margin of error\n")

    def DEVMODE(self):
        print(self.data)
        print("\n")
        print(self.YTD_rows)


if __name__ == "__main__":

    tickers = {"VBTLX":["https://investor.vanguard.com/investment-products/mutual-funds/profile/vbtlx#distributions","distributions",-1.01,.1]}

    ticker = "VBTLX"
    url = tickers[ticker][0]
    table = tickers[ticker][1]
    actual = tickers[ticker][2]
    epsilon = tickers[ticker][3]

    VBTLX = Tickers(ticker,url,table,epsilon,actual)
    asyncio.run(VBTLX.scrape_vanguard_data())
    f_t = VBTLX.f_total()
    VBTLX.assert_(f_t)