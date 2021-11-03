# MarketWatch-API

An API to retrieve general stock basic, and financial information from MarketWatch website.

This API only has two reference data: `/stock` amd `/stock/financial`

## `/stock`

The `/stock` reference provides the basic information of the specific stock using the `ticker` parameter. It will return a 200 status code with data like price, high, low, open, close, volume, etc. It is essentially what you can see on MarketWatch website whenever you search a ticker.

To call a `ticker` in `/stock`, you can call the Apple ticker like this:
`[url].com/stock?ticker=aapl`

\*Note: if `ticker` parameter is not provided, a 400 error will occur.

## `/stock/financial`

The `/stock/financial` reference provides all the financial data from MarketWatch website. The financial data consists of income statement, balance sheet, and cashflow.

The financial referece has three parameters: `ticker`, `finance` (optional), and `period` (optional). Both `finance` and `period` have default value.

To call a financial data, you can call for Apple's financial data like this:
`[url].com/stock/financial?ticker=aapl`

### Finance

The `finance` default value is `income` means "income statement". This will have the API call the default income statement of the company. The other values to check other financial data will be `balance` for balance sheet, and `cash` for cashflow. Any other values given out of `income`, `balance`, and `cash` will result in default value of `income`.

To call a financial data with different financial statement, you can call for Apple's financial data like this:
`[url].com/stock/financial?ticker=aapl&finance=balance`

To call

### Finance

The `period` default value is `annual` means the annual report. This will have the API call the default annual financial report of the company up to 5 years. There is only two values recognized by `period` parameter: `annual` and `quarter`. The `quarter` will show the quarterly report of the company. Any other values given out of `annual`, and `quarter` will result in default value of `annual`.

To call a financial data with different time period, you can call for Apple's financial data like this:
`[url].com/stock/financial?ticker=aapl&period=quarter`

Lastly you can interchangebly call it like this without having to place parameter accrdingly as long as the values are met properly:
`[url].com/stock/financial?ticker=aapl&period=quarter&finance=cash`

\*Note: if `ticker` parameter is not provided, a 400 error will occur.

# NOTE

NOTE: This is a personal hobby project. The technology behind this is solely webscrape on MarketWatch and parsing data back to the API calling. I will not hold any accountability for any information displacement as MarketWatch website will change in the future. You are free to fork, or join in to this "open-source" project to continuously improve or maintain the API.
