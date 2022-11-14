from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keys2 as keys2
from twilio.rest import Client

url = 'https://www.webull.com/quote/crypto'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')


# INSTRUCTIONS FOR PROJECT:
# Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies 
# and display as a formatted output one currency at a time. 
# The output should display the name of the currency, the symbol (if applicable), 
# the current price and % change in the last 24 hrs and corresponding price (based on % change) 
# Furthermore, for Bitcoin and Ethereum, the program should alert you via text if the value falls below $40,000 for BTC and $3,000 for ETH.

# Code for Project:

crypto_rows = soup.findAll('div',attrs={"class":"table-cell"})
counter = 1
counter_2 = 1

for row in range(5):
    symbol = crypto_rows[counter].text[0:7]
    name = crypto_rows[counter].text[7:]
    price = float(crypto_rows[counter+1].text)
    p_change = float(crypto_rows[counter+2].text.strip('%'))*0.01
    corr_price = (price * p_change) + price
    print(f"Symbol: {symbol}")
    print(f"Name: {name}")
    print(f"Current Price: ${price}")
    print(f"% Change: {p_change}")
    print(f"Corresponding Price: ${corr_price}")
    print()

    counter += 10

accountSID = ''
authToken = ''

client = Client(accountSID,authToken)

TwilioNumber = ''

myCellPhone = ''

for row in range(58):
    check = crypto_rows[counter_2].text
    price = float(crypto_rows[counter_2+1].text.replace(',',''))
    if check == 'BBTCUSDBitcoin' and price <= 40000:
        textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,
                body='Bitcoin is below $40,000')
    if check == 'EETHUSDEthereum' and price <= 3000:
        textmessage_2 = client.messages.create(to=myCellPhone,from_=TwilioNumber,
                body='Ethereum is below $3,000')

    counter_2 += 10
