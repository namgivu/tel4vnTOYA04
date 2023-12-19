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

s='1'   ; print( s.zfill(3) )
s='22'  ; print( s.zfill(3) )
s='333' ; print( s.zfill(3) )
