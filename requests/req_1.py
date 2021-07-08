import requests

site = 'https://ebay.com'

data = requests.get(site)

print(data.text)