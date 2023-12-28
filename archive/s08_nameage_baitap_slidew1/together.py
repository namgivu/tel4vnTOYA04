'''
Write a program that:
○ Input: name and year of birth.
○ Output: a string that “I am ... and I am ... years old.”
                              name         age
'''

# ref Phuong @ input name
name = input ('Enter name: ')

# ref Hieu kasumo @ input year
year = input('Enter year: ')

# ref Huynh kuzo @ get age
from datetime import date
today = date.today()
age = today.year - int(year)

# ref Mai Cuong @ print result
print(f'I am {name} and I am {age} years old.')
