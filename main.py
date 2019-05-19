from indicators import *
from constants import *
from coinbase import *
from debug import *
from helpers import *
import threading

# setup
fetch_accounts()

eth_account = accounts[eth]
btc_account = accounts[btc]

eth_ticker = Ticker(eth_usdc)
btc_ticker = Ticker(btc_usdc)

short_ema = EMA(10)
long_ema = EMA(20)

is_rising = False

price = 0

def update():
    global is_rising
    short_ema.add(eth_ticker.price)
    long_ema.add(eth_ticker.price)
    is_on_top = short_ema.ema > long_ema.ema

    if is_on_top and (not is_rising):
        # Starting to rise
        price = eth_ticker.price
        log('buy')
        log(price)
    elif (not is_on_top) and is_rising:
        # Starting to fall
        log('sell')
        log((eth_ticker.price - price)/eth_ticker.price)

    is_rising = is_on_top

def autofetch():
    eth_ticker.fetch()
    log(eth_ticker)
    update()
    threading.Timer(minutes(10), autofetch).start()

autofetch()


    









