import os

'''
ho=VU ten=Nam python ./s01_sys_argv.py
ho    ten     ...
'''
ho  = os.environ.get('ho')
ten = os.environ.get('ten')
print(f'Hi {ten} {ho}!')
