import requests

def test_index():
  res = requests.request('GET', 'http://127.0.0.1:5000')
  print(res)
  print(res.json() )


def test_github_latest_release():
  res = requests.request('GET', 'http://127.0.0.1:5000/github_latest_release')
  print(res)
  print(res.json() )
