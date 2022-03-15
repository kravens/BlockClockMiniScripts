# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 23:47:06 2022

@author: KevinR4v - Noderunner
"""
import requests

# Blockclock Mini local network name/address
address = input('Enter BlockClock Mini address (example 192.168.x.x):\n')

# Blockclock Mini password:
bc_pass = input('Enter BlockClock Mini password:\n')

# Text to display:
text = ''

# Or choose number to display:
number = '1'
pair = 'BTC/BTC'
sym = 'bitcoin'
tl = 'one bitcoin'
br = 'equals one btc'
URL = f'http://{address}/api/'

if text:
    URL += 'show/text/{}'.format(text)
elif number:
    URL += f'show/number/{number}'
    if pair:
        URL += f'?pair={pair}'
    if sym:
        URL += f'&sym={sym}'
    if tl:
        URL += f'&tl={tl}'
    if br:
        URL += f'&br={br}'

# Show generated URL:
print('\n Generated URL:',URL)

# Generate login token with password:
login = requests.auth.HTTPDigestAuth('admin', bc_pass)

# Update Blockclock mini with URL:
requests = requests.get(URL, auth=login)

# Show response:
#print(requests.text) # use this for debugging
happy = requests.text
if happy.split(',')[-1] == ' "status": "Worked"}\n\n':
    print('\n Happy BlockClock!')
else:
    print('\n Sad BlockClock... try again')
    print(happy.split(':')[-1].replace('}',''))