"""
: create venv
./venv/bin/python         -m pip install requests python-dotenv
./venv/Scripts/python.exe -m pip install requests python-dotenv
"""
import os
import requests


from dotenv import load_dotenv ; load_dotenv() ;   access_token = os.environ.get('access_token')

owner_repo = 'pyenv/pyenv'
headers    = {'Authorization': f'token {access_token}'}
url        = f'https://api.github.com/repos/{owner_repo}/releases/latest'

res = requests.request('GET', url, headers=headers)
d   = res.json()

print(f'''
--- latest git repo 's release
{d.get('name') }
{d.get('created_at') }
''')
