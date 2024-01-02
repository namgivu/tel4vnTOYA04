import os
import requests
from dotenv import load_dotenv ; load_dotenv() ;   access_token = os.environ.get('access_token')


def get_github_latest_release():
  owner_repo = 'pyenv/pyenv'
  url        = f'https://api.github.com/repos/{owner_repo}/releases/latest'
  headers    = {'Authorization': f'token {access_token}'}  #NOTE musthave auth in header or we get rate limitted request

  res = requests.request('GET', url, headers=headers)
  d   = res.json()

  return {
    'name':       d.get('name'),
    'created_at': d.get('created_at'),
  }
