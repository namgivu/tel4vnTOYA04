'''
5. Write a function that can 
calculate the sum of all even numbers 
from 1 to 10 with “for” loop.
'''

# by Nam
print(
  sum( [i for i in range(1,11) if i%2==0] )
)
