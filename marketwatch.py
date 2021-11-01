import requests, bs4

def request(url):
    r = requests.get(url).text
    soup = bs4.BeautifulSoup(r, 'html.parser')
    return soup

class marketwatch:
    def __init__(self, ticker):
        self.ticker = ticker

    def url(self):
        url = f'https://www.marketwatch.com/investing/stock/{self.ticker}'
        r = request(url)
        return r

    def accounting(self, finance, period=''):
        financials = f'/financials/{finance}'
        return url(self.ticker) + financials + f'/{period}' if (period == 'quarter') else url(self.ticker) + financials

    def data(self):
        info = [i.get_text() for i in self.url().find_all('span', {'class' : 'primary'})]
        close = [i.get_text() for i in self.url().find_all('td', {'class' : 'table__cell u-semi'})]
        data = {
                'status'        :   self.url().find_all('div', { 'class' : 'status' })[0].get_text(),
                'price'         :   round(float(self.url().find_all('bg-quote', { 'class' : 'value' })[0].get_text().replace('$', '').replace(',','')),2),
                'open'          :   round(float(info[6].replace('$', '').replace(',','')),2) if info[6] != "N/A" else "N/A",
                'high'          :   round(float(info[3].replace('$', '').replace(',','')),2) if info[3] != "N/A" else "N/A",
                'low'           :   round(float(info[2].replace('$', '').replace(',','')),2) if info[2] != "N/A" else "N/A",
                'close'         :   round(float(close[0].replace('$', '').replace(',','')),2) if info[0] != "N/A" else "N/A",
                'dividend'      :   round(float(info[-5].replace('$', '').replace(',','')),2) if info[-5] != "N/A" else "N/A",
                'volume'        :   info[1].split(':')[-1].strip() if info[1] != "N/A" else "N/A",
                'market_cap'    :   info[9] if info[9] != "N/A" else "N/A",
                'pe_ratio'      :   round(float(info[14]),2) if info[14] != "N/A" else "N/A",
                'beta'          :   round(float(info[12]),2) if info[12] != "N/A" else "N/A"
        }
        return data