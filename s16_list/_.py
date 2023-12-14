l = [1,22,333, 4,55,666]
# =  0 1  2    3 4  5
# =  0           -2 -1

print( l[0] )
print( l[5] )
print( len(l) )
print( l[-1] )
print( l[-2] )

print()  ###

print( l[0:1] )
print( l[0:0+1] )
print( l[0:1+1] )
print( l[0:2+1] )

print()  ###

print( l[2:4] )
print( l[2:3+1] )
print( l[1:5] )

print()  ###

print( l[0:-1] )
print( l[0:-2+1] )
print( l[0:-2] )
print( l[0:-3+1] )

print()  ###

print( l[0:]  )  # macdinh sau   : la cuoicung ie len(l)+1
print( l[ :2] )  # macdinh truoc : la 0
