from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

url = 'https://www.cryptocurrenc-y.com/top5ranking/'
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





message = ''

print(message)

# Twillio Text Code:

import temp.keys2 as keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = '+17432025260'

myCellPhone = '+18326490489'

textmessage = client.messages.create(to=myCellPhone,from_=TwilioNumber,
                body=message)

print(textmessage.status)