print( "hello" == 'hello' )
print( "hello" == 'Hello' )

b = "hello" == 'hello'
print(b)
print(f'{b=}')

print( (not True) and (not False) )
print( (1<2) and (2>3) )
print( (1<2) or  (2>3) )

###

if False: print(1)
else:     print(0)

if "": print(1)
else:  print(0)

if '': print(1)
else:  print(0)

if 'hello': print(1)
else:       print(0)
