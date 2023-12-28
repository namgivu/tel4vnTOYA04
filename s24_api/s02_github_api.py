import requests

'''
eg latest tag   https://api.github.com/repos/OWNER/REPO/git/tags
eg user's repo  https://api.github.com/users/tel4vn/repos
'''

u   = 'tel4vn'
res = requests.request(method='GET', url=f'https://api.github.com/users/{u}/repos')

d = res.json()
d = [e.get('full_name') for e in d]
print(d)

debug=122