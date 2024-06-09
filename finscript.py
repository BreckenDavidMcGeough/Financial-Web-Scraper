import asyncio
from requests_html import AsyncHTMLSession
import pandas as pd

data = []

async def scrape_vanguard_data():
    asession = AsyncHTMLSession()

    url = "https://investor.vanguard.com/investment-products/mutual-funds/profile/vbtlx#distributions"
    response = await asession.get(url)
    await response.html.arender(timeout=20)

    dist_table = response.html.find("distributions", first=True)
    if dist_table:
        print("Distributions table found")
        rows = dist_table.find("tr")
        for i in range(len(rows)):
            data.append(rows[i].text)

    await asession.close() 

def split_row_elem(elem):
    split_elem = elem.splitlines()
    return split_elem

def parse_arr():
    parsed = []
    for elem in data:
        parsed.append(split_row_elem(elem))
    return parsed

def sum_ppshare():
    sum_ = 0
    processed = parse_arr()
    processed.pop(0)
    for col in processed:
        if col[3][9] == '4':
            print(col)
            sum_ += float(col[1][1:])
    return sum_

def f_total():
    sum_ = sum_ppshare()
    start = 9.66
    end = 9.42
    total = ((sum_ + end) - start) / start 
    return round(total * 100,2)

if __name__ == "__main__":
    asyncio.run(scrape_vanguard_data())
    print(f_total())
   