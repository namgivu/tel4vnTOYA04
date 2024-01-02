import requests

res = requests.request('GET', 'http://127.0.0.1:5000')
print(res)
print(res.json() )
