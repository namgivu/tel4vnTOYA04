"""
shell cmd
ls -l

in python, how?
"""
import subprocess
subprocess.run(['ls', '-l'])
print()
subprocess.run(['ls'])

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
r = subprocess.run(['cat', '/some/notexists/file'], capture_output=True)
print(r)
r'''
CompletedProcess(args=['cat', '/some/notexists/file'], returncode=1, stdout=b'', 
                                                                     stderr=b'cat: /some/notexists/file: No such file or directory\n')
'''

print()
r = subprocess.run(['ls', '-l'], capture_output=True)
print(f'''
{r.returncode=}
{r.stdout.decode()=:>}
{r.stderr.decode()=:>}
''')
