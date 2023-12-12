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
