"""
shell cmd
ls -l

in python, how?
"""
import subprocess
subprocess.run(['ls', '-l'])
print()
subprocess.run(['ls'])


### intro capture_output=True

'''
r = subprocess.run(['ls'])

can see in r
-rw-rw-r-- 1 namgivu namgivu 119 Dec 26 20:52 _.py

trong r
stdout
stderr
'''
r = subprocess.run(['ls', '-l'], capture_output=True)
print(r)
r'''
CompletedProcess(args=['ls', '-l'], returncode=0, stdout=b'total 4\n-rw-rw-r-- 1 namgivu namgivu 374 Dec 26 20:56 _.py\n', 
                                                  stderr=b'')
'''

print()
r = subprocess.run(['ls', '/some/notexists/file'], capture_output=True)
print(r)
r'''
CompletedProcess(args=['ls', '/some/notexists/file'], returncode=1, stdout=b'', 
                                                                     stderr=b'cat: /some/notexists/file: No such file or directory\n')
'''

print()
r = subprocess.run(['ls', '-l'], capture_output=True)
print(f'''
{r.returncode=}
{r.stdout.decode()=:>}
{r.stderr.decode()=:>}
''')

### intro text=True

r = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(f'''
{r.returncode=}
{r.stdout=:>}
{r.stderr=:>}
''')  # will raise error > TypeError: unsupported format string passed to bytes.__format__

### intro check=True

print()
r = subprocess.run(['ls', '/some/notexists/file'], capture_output=True)
print(r)

# this will fail the running code if shellcmd fails
# r = subprocess.run(['ls', '/some/notexists/file'], capture_output=True, check=True)

print()
try:
  r = subprocess.run(['ls', '/some/notexists/file'], capture_output=True, check=True)
except:
  print('--- ERROR occurred')
  print(r)


### intro shell=True used w/ linux cmd pipe
'''
revisit linux cmd pipe

ls -l
ls -l | tail -n1
ls -l | tail -n2
ls -l | head -n2

ls /koco
ls /koco      | grep No
ls /koco 2>&1 | grep No
'''
print()
# r=subprocess.run('ls -l | wc -l', capture_output=True)  # error > FileNotFoundError: [Errno 2] No such file or directory: 'ls -l | wc -l'
r=subprocess.run('ls -l | wc -l', capture_output=True, shell=True)
print(r)
r=subprocess.run('ls -l',         capture_output=True, shell=True)
print(r)

print()
r=subprocess.run('ls -l; echo 122', capture_output=True, shell=True) ; print(r)
#                      ; CAUTION this can be used as injection attack
