import requests

url = "http://finance.google.com/finance/historical"

params = {}
params['q'] = 'TSLA'
params['startdate'] = '2016-01-01'
params['output'] = 'csv'

r = requests.get(url, params=params)

print(r.text)
