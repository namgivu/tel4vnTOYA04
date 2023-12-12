import random

for _ in range(6):
  print( random.randint(0,3) )

print()

for _ in range(6):
  print( random.randrange(0,6+1, step=2))  # same as randint() but can have :step param

print()

l = [1,22,333]
random.shuffle(l)
print(l)
