### print ruler
def print_ruler(c='.'):
  for _ in range(4):
    for i in range(10): print(_,end='')
  print()


  for _ in range(4): print( str(_).ljust(10,c),end='')
  print()

  for _ in range(4): print( str(_).rjust(10,c),end='')
  print()

  for _ in range(4):
    print( str(_).ljust(10-1,c),end='')
    print( str(_),                end='')

  print()

  for _ in range(4):
    for i in range(10): print(i,end='')
  print()


###
print_ruler()

s = 'python for devops'
print(s)
print(s.ljust(22,'.'),end='') ; print()
print(s.rjust(22,'.'),end='') ; print()


###
print()
print_ruler(c='-')

print(f'{s}')

print(f'{s: >22}')
print(f'{s:.>22}')

print(f'{s:<22}')
print(f'{s:.<22}')
