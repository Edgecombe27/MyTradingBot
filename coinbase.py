import cbpro
import os
from constants import *

key = os.environ['CBPRO_API_KEY']
secret = os.environ['CBPRO_SECRET']
passphrase = os.environ['CBPRO_PASSPHRASE']

public_client = cbpro.PublicClient()
auth_client = cbpro.AuthenticatedClient(key, secret, passphrase)

accounts = {}

class Ticker:

    # variables
    product = ''
    bid = 0
    ask = 0
    volume = 0
    price = 0

    # initializer
    def __init__(self, id):
        self.product = id
        self.fetch()
        

    # methods

    def fetch(self):
        data = public_client.get_product_ticker(product_id=self.product)
        self.bid = float(data['bid'])
        self.ask = float(data['ask'])
        self.volume = float(data['volume'])
        self.price = float(data['price'])

    def spread(self):
        return (self.ask - self.bid) / self.bid * 100

    def __str__(self):
        return self.product + ': bid: ' + str(self.bid) + ', ask: ' + str(self.ask) + ', price: ' + str(self.price) + ', volume: ' + str(self.volume)


def fetch_accounts():
    data = auth_client.get_accounts()
    for account in data:
        accounts[account['currency']] = Account(account)

class Account:

    # variables
    currency = ''
    balance = 0
    id = 0

    # initializer
    def __init__(self, data):
        self.currency = data['currency']
        self.balance = float(data['balance'])
        self.id = data['id']

    # methods
    def fetch(self):
        data = auth_client.get_account(self.id)
        self.currency = data['currency']
        self.balance = float(data['balance'])
        self.id = data['id']

    def __str__(self):
        return 'currency: '+self.currency+', balance: '+str(self.balance)

class Order:
    product = ''
    id = ''
    price = 0
    size = 0
    fee = 0
    filled = False

    def __init__(self, data):
        self.product = data['product_id']
        self.price = data['price']
        self.side = data['side']
        self.size = float(data['size'])
        self.id = data['id']
        self.status = data['status']
    
    def cancel(self):
        data = auth_client.cancel_order(self.id)

    def get_status(self):
        data = auth_client.get_order(self.id)
        self.status = data['status']
        return self.status

    def close(self):
        side = 'sell'
        if self.side == 'sell':
            side = 'buy'
        data = auth_client.place_limit_order(product_id=self.product, side=side, price=self.price, size=self.size)
        order = Order(data)
        return order

    def __str__(self):
        return 'product: '+self.product+', price: '+str(self.price)+', side: '+self.side+', size: '+str(self.size)+', status: '+self.status

def buy(self, product, price, size):
    data = auth_client.place_limit_order(product_id=product, side='buy', price=price, size=size)
    order = Order(data)
    return order

def sell(self, product, price, size):
    data = auth_client.place_limit_order(product_id=product, side='sell', price=price, size=size)
    order = Order(data)
    return order
  


