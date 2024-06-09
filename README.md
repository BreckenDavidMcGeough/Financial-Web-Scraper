# Financial Data Web Scraper

## A Python script that scrapes the VBTLX website for financial data

This script loads this website: [link](https://investor.vanguard.com/investment-products/mutual-funds/profile/vbtlx#distributions) and scrapes the 'Dividend income and capital gains' section of the page. The script is asynchronous and utitlizes asyncio and AsyncHTMLSession to do this, since the data is generated dynamically on the page. It then isolates the rows in an array starting from the current date, all the way to the first day of 2024 (YTD). Then it parses each row in the array to get the $/share, summing their total in a variable named sum_. Then it calculates the total price YTD using the equation: ((sum_ + end - start) / start) * 100. Start and end are variables that store the close price on the first day of 2024, and the current day respectively (rounded to the last market day).

I also included a pdf of a design, analaysis, and proof of correctness for an optimal stock portfolio building algorithm based off of the fractional knapsack problem. It is titled 'cse431hw3-11.pdf'.
