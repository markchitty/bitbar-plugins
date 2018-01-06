# Bitbar Plugins

## Coinmarketcap rates

![Coinmarketcap rates](https://i.imgur.com/UnAYPVr.png "Coinmarketcap rates")

At the top of the script, edit the crypto currency list and display currency to show the rates you're following.

```python
# Just add the currency codes for the crypto currencies you want to track
crypto_currencies     = ['ETH', 'LTC', 'TRX', 'XVG']

# And set the currency code and symbol for the fiat currency you want to see prices in
# USD fx rates are fetched from fixer.io
display_currency_code = 'EUR'
display_symbol        = '€'

