#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# <bitbar.title>Coinmarketcap rates</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>markjchitty</bitbar.author>
# <bitbar.desc>Displays Cryptocurrency rates from coinmarketcap, in any fiat (USD, EUR, GBP, etc)</bitbar.desc>
# <bitbar.image>https://i.imgur.com/UnAYPVr.png</bitbar.image>
# <bitbar.dependencies>python</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/markchitty/bitbar-plugins</bitbar.abouturl>
#
# by Alvin
import urllib2
from json import JSONDecoder

# Just add the currency codes for the crypto currencies you want to track
crypto_currencies     = ['ETH', 'LTC', 'TRX', 'XVG']

# And set the currency code and symbol for the fiat currency you want to see prices in
# USD fx rates are fetched from fixer.io
display_currency_code = 'EUR'
display_symbol        = '€'

def index(arr, func):
     return next((i for i in xrange(len(arr)) if func(arr[i])), None)

def get_item(arr, symbol):
     return arr[index(arr, lambda item: item['symbol'] == symbol)]

def get_price(crypto_rates, crypto_code, fxrate):
    crypto_data = get_item(crypto_rates, crypto_code)
    price = float(crypto_data['price_usd']) * float(fxrate)
    price_mbtc = float(crypto_data['price_btc']) * 1000
    extra_info = ' / m₿{:.5g} ({})'.format(price_mbtc, crypto_data['name'])
    if crypto_code == 'BTC': extra_info = ''
    return '{}: {}{:,.5g}{}'.format(crypto_code, display_symbol, price, extra_info)

try:
    request = urllib2.Request(url='https://api.coinmarketcap.com/v1/ticker/')
    response = urllib2.urlopen(request).read()
    coinmarketcap_rates = JSONDecoder().decode(response)

    if display_currency_code == 'USD':
        usd_rate = 1
    else:
        request = urllib2.Request(url='https://api.fixer.io/latest?base=USD&symbols=' + display_currency_code)
        response = urllib2.urlopen(request).read()
        usd_rate = JSONDecoder().decode(response)['rates'][display_currency_code]

    print(get_price(coinmarketcap_rates, 'BTC', usd_rate))
    print('---')
    for cur in crypto_currencies:
        print(get_price(coinmarketcap_rates, cur, usd_rate))

except Exception as e:
    print('{}'.format(e))