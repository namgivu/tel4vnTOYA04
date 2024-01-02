"""
Create a command line tool in python, having these features:
○ Get the latest tag of given repository name.
○ Create new tag, by increase the latest tag by 1.

■ Example: latest tag: v2 -> new tag will be v3
○ Make a new release from a tag.
■ Use release name from user input.
■ If not, auto generate release name by format "release/dd-mm-yy"
"""
import json

import requests


owner_repo = 'pyenv/pyenv'


'''latest tag @ thru github api url'''
def get_latest_tag__by_github_api():
  d_list = []
  while True:
    pagination = 'page=2'
    url        = f'https://api.github.com/repos/{owner_repo}/tags?{pagination}'
    '''eg          https://api.github.com/repositories/5625464/tags?page=2'''

    res = requests.request(method='GET', url=url)
    d   = res.json()

    d_list.extend([d])

    print(len(d_list))

    next_link = res.links.get('next', {})
    if not next_link: break
    else:             url = next_link.get('url')


  print(d_list)
  # d = [e.get('name') for e in d]
  debug=122
# get_latest_tag()
# issue  > {'message': "API rate limit exceeded for 113.172.192.123. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)",

'''
can code continue w/ api response at limited rate
BUT let's switch to PyGithub package 
'''
d_origin = res_json = [
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  [
    {
      "name": "v20141011",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141011",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141011",
      "commit": {
        "sha": "d38f00cd4a6ca47ee94f49d99534d8d899ffc71f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d38f00cd4a6ca47ee94f49d99534d8d899ffc71f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDEx"
    },
    {
      "name": "v20141008",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20141008",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20141008",
      "commit": {
        "sha": "ff995b66548b00d7ef878a5b6e18b128d0e08e8f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ff995b66548b00d7ef878a5b6e18b128d0e08e8f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQxMDA4"
    },
    {
      "name": "v20140924",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140924",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140924",
      "commit": {
        "sha": "ab9ee414ad836ea21950ed44eeb77a5b272a6549",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/ab9ee414ad836ea21950ed44eeb77a5b272a6549"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwOTI0"
    },
    {
      "name": "v20140825",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140825",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140825",
      "commit": {
        "sha": "6509d318f4d70f838cf66683931049379e06d703",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6509d318f4d70f838cf66683931049379e06d703"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwODI1"
    },
    {
      "name": "v20140705",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140705",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140705",
      "commit": {
        "sha": "b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/b8a7de8a3ce2207eb5ca42e80becb17f1fbd98c6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNzA1"
    },
    {
      "name": "v20140628",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140628",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140628",
      "commit": {
        "sha": "0468ffdd4970f564fd9c19c171dd4b947ee4819e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0468ffdd4970f564fd9c19c171dd4b947ee4819e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjI4"
    },
    {
      "name": "v20140615",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140615",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140615",
      "commit": {
        "sha": "21c0d930e9923da2c36b033fcb663e3cc9c00c3d",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/21c0d930e9923da2c36b033fcb663e3cc9c00c3d"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE1"
    },
    {
      "name": "v20140614",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v20140614",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v20140614",
      "commit": {
        "sha": "2b5ee0c425db820493fc3585e58bf921bdccc3fc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2b5ee0c425db820493fc3585e58bf921bdccc3fc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIwMTQwNjE0"
    },
    {
      "name": "v2.3.35",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.35",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.35",
      "commit": {
        "sha": "74a2523c97d2e5c1dbdca7b58f3372324ccad4e6",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/74a2523c97d2e5c1dbdca7b58f3372324ccad4e6"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNQ=="
    },
    {
      "name": "v2.3.34",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.34",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.34",
      "commit": {
        "sha": "d3766f22a588519cb640771130fa8ed6985f0556",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d3766f22a588519cb640771130fa8ed6985f0556"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zNA=="
    },
    {
      "name": "v2.3.33",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.33",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.33",
      "commit": {
        "sha": "2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/2fb5b9e9a3c498dbc74c3452851ff90c95dcdc5a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMw=="
    },
    {
      "name": "v2.3.32",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.32",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.32",
      "commit": {
        "sha": "d31230109957392ddf178ddfe78db195afbe8ccf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/d31230109957392ddf178ddfe78db195afbe8ccf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMg=="
    },
    {
      "name": "v2.3.31",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.31",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.31",
      "commit": {
        "sha": "54f7a7c0464f4feb3ba61cfee72fc14db802f98f",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/54f7a7c0464f4feb3ba61cfee72fc14db802f98f"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4zMQ=="
    },
    {
      "name": "v2.3.29",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.29",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.29",
      "commit": {
        "sha": "bb38acd99460f6dd2c5367cbc28947c4ef2fc209",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bb38acd99460f6dd2c5367cbc28947c4ef2fc209"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOQ=="
    },
    {
      "name": "v2.3.28",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.28",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.28",
      "commit": {
        "sha": "28e7000b485bff61235d8a691c3989c9a5ed0a53",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/28e7000b485bff61235d8a691c3989c9a5ed0a53"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yOA=="
    },
    {
      "name": "v2.3.27",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.27",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.27",
      "commit": {
        "sha": "c844b332ca9744ee5273a8c40396f29b0d730bdf",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/c844b332ca9744ee5273a8c40396f29b0d730bdf"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNw=="
    },
    {
      "name": "v2.3.26",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.26",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.26",
      "commit": {
        "sha": "bdfb80cc129d0aed666700d582a42d19cc7902a1",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/bdfb80cc129d0aed666700d582a42d19cc7902a1"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNg=="
    },
    {
      "name": "v2.3.25",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.25",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.25",
      "commit": {
        "sha": "7ec5c30451393d21ddc1e3ed5a588b717d77305e",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7ec5c30451393d21ddc1e3ed5a588b717d77305e"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNQ=="
    },
    {
      "name": "v2.3.24",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.24",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.24",
      "commit": {
        "sha": "79a501139fd106b39c6095467930ac506822c4c5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/79a501139fd106b39c6095467930ac506822c4c5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yNA=="
    },
    {
      "name": "v2.3.23",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.23",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.23",
      "commit": {
        "sha": "879fa68b35608672b1b979f0e5665a6a506e1366",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/879fa68b35608672b1b979f0e5665a6a506e1366"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMw=="
    },
    {
      "name": "v2.3.22",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.22",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.22",
      "commit": {
        "sha": "af1a54482b00027e5dba533477aced2f358691f5",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/af1a54482b00027e5dba533477aced2f358691f5"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMg=="
    },
    {
      "name": "v2.3.21",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.21",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.21",
      "commit": {
        "sha": "7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/7c17c741ebe6fb94e35ef2e74d92fe1300fbcdef"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMQ=="
    },
    {
      "name": "v2.3.20",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.20",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.20",
      "commit": {
        "sha": "43f40eca05aec7d01d09ebb15005aacd5a44c518",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/43f40eca05aec7d01d09ebb15005aacd5a44c518"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4yMA=="
    },
    {
      "name": "v2.3.19",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.19",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.19",
      "commit": {
        "sha": "e79dd97afa8ee1cc696fe70696f466f34cff5874",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/e79dd97afa8ee1cc696fe70696f466f34cff5874"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOQ=="
    },
    {
      "name": "v2.3.18",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.18",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.18",
      "commit": {
        "sha": "3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/3fa5812bfcfe53e022c9e6ff5de18f342ac0b6d9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xOA=="
    },
    {
      "name": "v2.3.17",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.17",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.17",
      "commit": {
        "sha": "9a4f9c2511f39701cb8e3af1e6809be28210c3b9",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9a4f9c2511f39701cb8e3af1e6809be28210c3b9"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNw=="
    },
    {
      "name": "v2.3.16",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.16",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.16",
      "commit": {
        "sha": "9fad1f46c50526df1fa3a5fd8188e785bb530b9c",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/9fad1f46c50526df1fa3a5fd8188e785bb530b9c"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNg=="
    },
    {
      "name": "v2.3.15",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.15",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.15",
      "commit": {
        "sha": "6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/6bb75b3ba79a7f9b6c2eae7fe2d7521e315cc04a"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNQ=="
    },
    {
      "name": "v2.3.14",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.14",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.14",
      "commit": {
        "sha": "904dd5f828fb4b4eccd643270834d38fd3764261",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/904dd5f828fb4b4eccd643270834d38fd3764261"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xNA=="
    },
    {
      "name": "v2.3.13",
      "zipball_url": "https://api.github.com/repos/pyenv/pyenv/zipball/refs/tags/v2.3.13",
      "tarball_url": "https://api.github.com/repos/pyenv/pyenv/tarball/refs/tags/v2.3.13",
      "commit": {
        "sha": "0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc",
        "url": "https://api.github.com/repos/pyenv/pyenv/commits/0ab9683e58b75fd3ee4f5a8b9f3a33d8e3f701bc"
      },
      "node_id": "MDM6UmVmNTYyNTQ2NDpyZWZzL3RhZ3MvdjIuMy4xMw=="
    }
  ],
  {
    "message": "API rate limit exceeded for 113.172.192.123. (But here's the good news: Authenticated requests get a higher rate limit. Check out the documentation for more details.)",
    "documentation_url": "https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting"
  }
]
d = d_origin[:-1]  # d aka data
