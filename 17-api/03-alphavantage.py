import requests

api_key = "67U0K6CDYAFV7N6M"

def get_intraday_stock_prices(symbol, interval, api_key):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        stock_data = response.json()['Time Series ({})'.format(interval)]
        for date, data in stock_data.items():
            open_price = data['1. open']
            high_price = data['2. high']
            low_price = data['3. low']
            close_price = data['4. close']

            print(f"Date: {date}")
            print(f"Open: {open_price}")
            print(f"High: {high_price}")
            print(f"Low: {low_price}")
            print(f"Close: {close_price}")
            print("------")
    else:
        print("API error")
import requests

def get_global_quote(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        quote_data = response.json()['Global Quote']
        open_price = quote_data['02. open']
        high_price = quote_data['03. high']
        low_price = quote_data['04. low']
        current_price = quote_data['05. price']
        
        
        print(f"Open: {open_price}")
        print(f"High: {high_price}")
        print(f"Low: {low_price}")
        print(f"Current Price: {current_price}")
        
    else:
        print("API error")

def get_exchange_rate(from_currency, to_currency, api_key):
    url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        exchange_data = response.json()['Realtime Currency Exchange Rate']
        from_code = exchange_data['1. From_Currency Code']
        from_name = exchange_data['2. From_Currency Name']
        to_code = exchange_data['3. To_Currency Code']
        to_name = exchange_data['4. To_Currency Name']
        exchange_rate = exchange_data['5. Exchange Rate']

        print(f"From Currency: {from_code} ({from_name})")
        print(f"To Currency: {to_code} ({to_name})")
        print(f"Exchange Rate: {exchange_rate}")

    else:
        print("API error")

def get_sector_performance(api_key):
    url = f"https://www.alphavantage.co/query?function=SECTOR&apikey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        sector_data = response.json()['Rank A: Real-Time Performance']
        for sector, performance in sector_data.items():
            performance_percent = performance[:-1]  

            print(f"Sector: {sector}")
            print(f"Performance: {performance_percent}%")
            print("------")
    else:
        print("API error")

# get_sector_performance(api_key)


def get_stock_news(symbol, api_key):
    url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={symbol}&apikey={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        print(response.json())
        news_data = response.json()['feed']
        for news in news_data:
            # Extract the information you need from each news article dictionary
            title = news['title']
            source = news['source']
            link = news['url']
            # ... and so on
            
            # Print or use the retrieved information as needed
            print(f"Title: {title}")
            print(f"Source: {source}")
            print(f"Link: {link}")
            print("------")
    else:
        print("API error")

from_currency = "USD"
to_currency = "THB"
# get_exchange_rate(from_currency, to_currency, api_key)

symbol = "TSLA"
interval = "15min"
# get_intraday_stock_prices(symbol, interval, api_key)

symbol = "MSFT"
# get_global_quote(symbol, api_key)

symbol = "TSLA"
get_stock_news(symbol, api_key)