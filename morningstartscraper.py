from requests_html import HTMLSession
import pandas as pd
import time

class Tickers:
    def __init__(self,ticker,url):
        self.url = url
        self.data = []
        self.ticker = ticker
        self.dates_dict = {'1-Day': 0, '1-Week': 1, '1-Month': 2, '3-Month': 3, 'YTD': 4, '1-Year': 5, '3-Year': 6, '5-Year': 7, '10-Year': 8, '15-Year': 9}

    def scrape_vanguard_data(self):
        session = HTMLSession()

        for _ in range(100):
            response = session.get(self.url)
            response.html.render()

            time.sleep(2)

            dist_table = response.html.find("table.mds-table__sal.mds-table--fixed-column__sal", first=True)
            if dist_table:
                print("Table found")
                rows = dist_table.find("tr.mds-tr__sal")
                for row in rows:
                    cells = row.find("td")
                    row = []
                    for cell in cells:
                        row.append(cell.text)
                        #print(cell.text)
                    self.data.append(row)
                break  
            else:
                print("Table not found: retrying...")

    def get_investment_by_date(self,date):
        investments = self.data[0]
        index = self.dates_dict[date] + 1
        return investments[index]


def Test(ticker):
    url = "https://www.morningstar.com/funds/xnas/" + ticker + "/performance"

    tick = Tickers(ticker,url)
    tick.scrape_vanguard_data()

    dates = ['1-Day', '1-Week', '1-Month', '3-Month', 'YTD', '1-Year', '3-Year', '5-Year', '10-Year', '15-Year']
    print(ticker + "---------------------------------------------")
    for date in dates:
        print(str(tick.get_investment_by_date(date)) + " : " + date)  
    print("-------------------------------------------------\n") 


if __name__ == "__main__":

    tickers = ["brsix","vbtlx","vsmpx","vtsax"]
    for ticker in tickers:
        Test(ticker)