"""
# project-wise folder-wise
python -m pip install --upgrade pip virtualenv
python -m virtualenv venv
./venv/bin/python         -m pip install requests python-dotenv
./venv/Scripts/python.exe -m pip install requests python-dotenv


# system-wise
python -m pip install requests
"""
import requests

# call endpoint in slide 4.x
res = requests.request(method='GET', url='https://api.upcitemdb.com/prod/trial/lookup?upc=190199267961')
print(res)
print(f'{res.status_code=}')
print(f'{res.text=}')

import json
d = json.loads(res.text)
print(d)
print(json.dumps(d, indent=2)[:122] + '\n  ...\n}')

print()

# requests.request(url='https://api.upcitemdb.com/prod/trial/lookup?upc=190199267961')  # error > TypeError: request() missing 1 required positional argument: 'method'
r = requests.get(url='https://api.upcitemdb.com/prod/trial/lookup?upc=190199267961')  # error > TypeError: request() missing 1 required positional argument: 'method'
j = r.json()  # shorthand for json.loads(r.text)
print(j)
