import requests

'''
eg latest tag   https://api.github.com/repos/OWNER/REPO/git/tags
eg user's repo  https://api.github.com/users/tel4vn/repos
'''

def get_user_repo_on_github(u):
  res = requests.request(method='GET', url=f'https://api.github.com/users/{u}/repos')

  d = res.json()
  d = [e.get('full_name') for e in d]
  print(d)

get_user_repo_on_github(u='tel4vn')
