'''
5. Write a function that can
calculate the sum of all even numbers
from 1 to 10 with “for” loop.
'''

# by Phuong
s=0
for i in range(1,11):
  if i%2==0:
    s=s+i
  print()

print(f'tong la: {s}')
