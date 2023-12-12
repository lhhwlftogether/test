import requests

from concurrent.futures import ThreadPoolExecutor

def fetch_url(url):

    response = requests.get(url)

    return response.text

urls = ['https://api-gcp.binance.com/api/v3/historicalTrades?symbol=BTCUSDT&limit=10', 'https://api-gcp.binance.com/api/v3/historicalTrades?symbol=LINKUSDT&limit=10']

with ThreadPoolExecutor() as executor:

    results = executor.map(fetch_url, urls)
    print(results)
    print("==========")

    for result in results:
        print(result)