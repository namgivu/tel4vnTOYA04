import os
f_path = f'{os.path.dirname(__file__)}/myfile.txt'

f = open(f_path)
fc = f.read()
f.close()

f = open(f_path)
line_list = f.readlines()
f.close()

###

with open(f_path) as f:
  line_list2 = f.readlines()

debug=122