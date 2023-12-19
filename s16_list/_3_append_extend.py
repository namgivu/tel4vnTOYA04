l = [1,22,333, 4,55,666]

print(l)
l.append('abb') ; print(l)
l    += ['ccc'] ; print(l)

l2 = ['x', 'yy']
l.extend(l2) ; print(l)


l.append([7,88]) ; print(l)  #CAUTION wrong result!
l.pop(-1)  # del at index last
l.extend([7,88]) ; print(l)  # now it's right

'''
conclusion 
.append()   single item
.extend()   multi item
'''

###
print()

l = [1,2,3,4,5,6]
print(l)    ; l.append(7)      ; print(l)
print(l)    ; l.append([7,8])  ; print(l)
# print(l)  ; l.append( 7,8 )  ; print(l)  #ERROR TypeError: list.append() takes exactly one argument (2 given)
print(l)    ; l.extend([7,8])  ; print(l)
print(l)    ; l.extend([7])    ; print(l)
# print(l)  ; l.extend( 7 )    ; print(l)  #ERROR TypeError: 'int' object is not iterable

###
print()

l = [1,2,3,4,5]
l2  = l.copy(); l2.append(6)      ; print(l2)
# l2= l.copy(); l2.append(6, 7)   ; print(l2)  #ERROR TypeError: list.append() takes exactly one argument (2 given)
l2  = l.copy(); l2.append([6, 7]) ; print(l2)
l2  = l.copy(); l2.extend([6, 7]) ; print(l2)
# l2  = l.copy(); l2.extend( 6, 7); print(l2)  #ERROR TypeError: list.extend() takes exactly one argument (2 given)
