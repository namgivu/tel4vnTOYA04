import requests
#
from dotenv import load_dotenv
import os


load_dotenv()
GITHUB_API_KEY=os.environ.get('GITHUB_API_KEY')

owner_repo = 'pyenv/pyenv'
pagination = 'page=1'
url        = f'https://api.github.com/repos/{owner_repo}/tags?{pagination}'  #TODO how to have &sort=created working?
headers    = {'Authorization': f'Bearer {GITHUB_API_KEY}' }

d_list = []
while True:
  print(f'{url=:>}')
  res = requests.request(method='GET', url=url, headers=headers)
  d   = res.json()
  d_list.extend([d])

  next_link = res.links.get('next', {})
  if not next_link: break
  else:             url = next_link.get('url')

print(d_list)
import json; print( json.dumps(d_list, indent=2, default=str) )
