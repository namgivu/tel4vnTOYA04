### endswith()
f='img.png'
if f.endswith('.txt'): print('Is text file')
else:                  print('Is NOT text file')

f='img.svg'
if f.endswith('.txt'): print('Is text file')
else:                  print('Is NOT text file')

f='a.txt'
if f.endswith('.txt'): print('Is text file')
else:                  print('Is NOT text file')

### zfill()
print()

s='1'   ; print( s.zfill(3) )
s='22'  ; print( s.zfill(3) )
s='333' ; print( s.zfill(3) )

###
#                   -1
#                 -2
#              -5
#            -7
#         -10
s = "This is a string"
#    0123456789012345
#    0         1

print( s[len(s)-1] )  # ref Huynh
print( s[-1] )        # ref Duy
print( s[5:7] )       # ref Hieu
print( s[10:] )       # ref Phuong
print( s[:9] )        # ref Huynh
#
print( f'{s[:]=}' )         # ref Duy
print( f'{s[-5:-7]=}' )     # ref Hieu
print( f'{s[-7:-5]=}' )
print( f'{s[-10:]=}' )      # ref Phuong
print( f'{s[:-9]=}' )       # ref Huynh
