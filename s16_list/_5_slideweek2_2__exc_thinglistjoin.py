"""
Given a list of things:
○ things = ['pen', 'ruler', 'wallet', 'phone']
● Write a function return the string contains all items, seperate
by comma (,), but the 'and' before the last item.
"""

things = ['pen', 'ruler', 'wallet', 'phone']


def ans01_use_join():
  print(things)
  print( ','.join(things) )
  print( ', '.join(things) )

  last_thing           = things[-1]     ; print(last_thing)
  allthing_but_thelast = things[0:-2+1] ; print(allthing_but_thelast)

  print(', '.join(allthing_but_thelast) + f', and {last_thing}')


def ans02_dontuse_join__practice_pylist_skill():
  kq = ''
  for th in things[:-2+1]:
    kq   +=  f'{th}, '
    # kq +=     th + ', '
    # kq = kq + th + ', '
    # print(th, end=', ')
  kq += f'and {things[-1]}'
  print(kq)
ans02_dontuse_join__practice_pylist_skill()
