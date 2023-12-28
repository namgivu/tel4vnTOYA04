"""
# project-wise folder-wise
python -m pip install --upgrade pip virtualenv
python -m virtualenv venv
./venv/Scripts/python.exe -m pip install requests


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
