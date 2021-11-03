# MarketWatch-API
An API to retrieve general stock basic, and financial information from MarketWatch website.

This API only has two reference data: `/stock` amd `/stock/financial`

## `/stock`
The `/stock` reference provides the basic information of the specific stock using the `ticker` parameter. It will return a 200 status code with data like price, high, low, open, close, volume, etc. It is essentially what you can see on MarketWatch website whenever you search a ticker.

To call a `ticker` in `/stock`, you can call the Apple ticker like this:
`[url].com/stock?ticker=aapl`

*Note: if `ticker` parameter is not provided, a 400 error will occur.

## `/stock/financial`
