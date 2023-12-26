'''
3) Exercise
Write a python script to call shell function `df -h`.

Using `argv` to receive an argument as 'mountedon'
if user not input, take the default as '/'.
Print the size and available spaces on that disk. If error, handle the error.

Filesystem      Size  Used Avail Use% Mounted on
udev            7,6G     0  7,6G   0% /dev
tmpfs           1,6G  2,5M  1,6G   1% /run
/dev/nvme0n1p2  1,9T   61G  1,7T   4% /
'''

#region handle input arg
'''
# argv
# 0  1 
_.py mountedon
_.py 
_.py /
_.py /dev
'''
import sys

try:    mountedon = sys.argv[1]
except: mountedon = '/'

print(f'{mountedon=:>}')
#endregion handle input arg

print()

#region parse data col
import subprocess

r = subprocess.run('df -h', shell=True, capture_output=True, text=True)
s = r.stdout
print(s)

lines = s.split('\n')[1:]
print(lines)

lines = [l.split() for l in lines]
print(lines)

lines_l = [
  [l[1],l[3], l[-1]]
  for l in lines
  if l
]
print(lines_l)

lines_l = [
  {
    'size'      : l[1],
    'avail'     : l[3],
    'mountedon' : l[-1],
  }
  for l in lines
  if l
]
print(lines_l)

'''
[ ['7,6G', '7,6G', '/dev'],                               ['1,6G', '1,6G', '/run'],                               ['1,9T', '1,7T', '/'],                               ['7,7G', '7,5G', '/dev/shm'], ['5,0M', '5,0M', '/run/lock'], ['7,7G', '7,7G', '/sys/fs/cgroup'], ['511M', '505M', '/boot/efi'], ['1,6G', '1,6G', '/run/user/1000']]
[ {'size': '7,6G', 'avail': '7,6G', 'mountedon': '/dev'}, {'size': '1,6G', 'avail': '1,6G', 'mountedon': '/run'}, {'size': '1,9T', 'avail': '1,7T', 'mountedon': '/'}, {'size': '7,7G', 'avail': '7,5G', 'mountedon': '/dev/shm'}, {'size': '5,0M', 'avail': '5,0M', 'mountedon': '/run/lock'}, {'size': '7,7G', 'avail': '7,7G', 'mountedon': '/sys/fs/cgroup'}, {'size': '511M', 'avail': '505M', 'mountedon': '/boot/efi'}, {'size': '1,6G', 'avail': '1,6G', 'mountedon': '/run/user/1000'}]
'''

print()
'''
mountedon -> {size, avail}
'''
lines_d = {
  e['mountedon'] : {'size': e['size'], 'avail': e['avail']}
  for e in lines_l
}
print(lines_d)

#endregion parse data col

print()

# output
r = lines_d.get(mountedon)
if r: print(f'Found data for {mountedon=:>}\n{r}')
else: print(f'Not found data for {mountedon=:>}')
