# Financial Data Web Scraper

## A Python script that scrapes the VBTLX website for financial data

The script 'finscript.py' loads this website: [link](https://investor.vanguard.com/investment-products/mutual-funds/profile/vbtlx#distributions) and scrapes the 'Dividend income and capital gains' section of the page. The script is asynchronous and utitlizes asyncio and AsyncHTMLSession to do this, since the data is generated dynamically on the page. It then isolates the rows in an array starting from the current date, all the way to the first day of 2024 (YTD). Then it parses each row in the array to get the $/share, summing their total in a variable named sum_. Then it calculates the total price YTD using the equation: ((sum_ + end - start) / start) * 100. Start and end are variables that store the close price on the first day of 2024, and the current day respectively (rounded to the last market day).

The script 'morningstarscraper.py' loads this website: [link](https://www.morningstar.com) and depending on which mutual fund investment data you want to view, will load the perfomance section of that mutual fund. For example, if you wish to view the data for VBTLX, then it will scrape the link: 

Morning Star VBTLX mutual fund: [https://www.morningstar.com/funds/xnas/vbtlx/performance](https://www.morningstar.com/funds/xnas/vbtlx/performance) 

It will return a list of all mutual funds that you desired to view, and for each mutual fund will display a list of the investment returns at days end for 1-day, 1-month, 3-montsh, YTD, 1-year, 3-year, 5-year, 10-year, 15-year timescale increments that it scraped from each mutual funds page on the morningstar website.

I also included a pdf of a design, analaysis, and proof of correctness for an optimal stock portfolio building algorithm based off of the fractional knapsack problem. It is titled 'cse431hw3-11.pdf'.
