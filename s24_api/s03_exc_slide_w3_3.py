"""
Create a command line tool in python, having these features:
○ Get the latest tag of given repository name.
○ Create new tag, by increase the latest tag by 1.

■ Example: latest tag: v2 -> new tag will be v3
○ Make a new release from a tag.
■ Use release name from user input.
■ If not, auto generate release name by format "release/dd-mm-yy"
"""
import requests

'''latest tag'''
def get_latest_tag():
  d_list = []
  while True:
    owner_repo = 'pyenv/pyenv'
    pagination = 'page=2'
    url        = f'https://api.github.com/repos/{owner_repo}/tags?{pagination}'
    '''pagination  https://api.github.com/repositories/5625464/tags?page=2'''

    res = requests.request(method='GET', url=url)
    d   = res.json()

    d_list.extend([d])

    print(len(d_list))

    next_link = res.links.get('next', {}).get('url')
    if not next_link: break


  print(d_list)
  # d = [e.get('name') for e in d]
  debug=122
# get_latest_tag()
# issue  > {'message': "API rate limit exceeded for 113.172.192.123. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
