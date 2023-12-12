#region demo datetime
'''get today date'''
#    package         module
from datetime import date
v = date.today() ; print(f'today is {v}')

'''get now time'''
from datetime import datetime
print(f'now is {datetime.now()}')

'''get timestamp'''
d = datetime.now()
print( datetime.strftime(d,                             '%Y%m%d_%H%M%S') )
print( datetime.strftime(datetime(2000,1,22),           '%Y%m%d_%H%M%S') )
print( datetime.strftime(datetime(2008,9,10, 11,12,13), '%Y%m%d_%H%M%S') )
#endregion demo datetime

print()


#region demo random
import random
print( random.randint(0,1) )
print( random.randrange(0,11, 2))  # same as randint() but can have :step param
#                           , 2==step

l = [1,22,333]
print( random.choice(l) )

#region codeforfun
_=''
_,                   l = _,[1,22,333]
print( random.choice(l) )

a = 1
b = 22
a,b = 1,22
#endregion codeforfun

print()
l = [1,22,333]    ; print(f'before shuffle {l=}')
random.shuffle(l) ; print(f'after  shuffle {l=}')

#endregion demo random
