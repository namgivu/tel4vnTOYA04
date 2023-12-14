import random

l = [66,1,4,2,3,6,5]

print(l)
print(sorted(l))

l_origin = l.copy()
print(f'{l_origin=}')

l.sort()
print(f'after l.sort()  {l=}')

print(f'{l_origin=}')

###

l2 = []

for i in l_origin:
  print(i)

  name = random.choice(['a','b','c'])

  l2.append(
    [i, name]
    #0  1     <-- x in lambda x below
  )

###

l2 = [
  [i, random.choice(['a','b','c']) ]
  for i in l_origin
]

print(       f'{l2=}')
print(f'{sorted(l2)=}')
print(   sorted(l2, key=lambda x: x[1]) )  # it's ok if you dont understand this now
