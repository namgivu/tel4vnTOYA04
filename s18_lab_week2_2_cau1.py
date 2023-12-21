"""
Giving url = "https://tel4vn.edu.vn/course/python-for-devops/"

Split the string to get
○ The protocol "https"
○ 3 parts of domain ["tel4vn", "edu", "vn"]
○ 2 parts of path ["course", "python-for-devops"]
"""

# ref Phuong

url = 'https://tel4vn.edu.vn/course/python-for-devops/'
#   =        01             2      3        

usp = url.split('/')
print('ketqua', usp[0][:-1])  # https: 
print(usp[2].split('.'))
print(usp[3:-1])
