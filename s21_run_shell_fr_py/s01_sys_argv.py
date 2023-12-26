import sys
print(sys.argv)

'''
python ./s01_sys_argv.py VU Nam
#      0                 1  2
'''
ho  = sys.argv[1]
ten = sys.argv[2]
print(f'Hi {ten} {ho}!')
