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
