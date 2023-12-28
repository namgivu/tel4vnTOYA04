"""
Write code that will do the following work:
○ Input ”n” as number of people.
○ Input ages of n people.

○ Ticket price is:
■ 100$ / 1 adult, 18 to 60 years old.
■ 25$/ 1 children, which is younger than 18.
■ 50$/1 person, which is older than 60.

○ Calculate the total money of those people’s tickets.
"""

# Input number of people
n = int(input('Input number of people: '))

# Input ages of people
ages = []
price = 0

for i in range(n):
  age = int(input(f'Input age of person {i + 1}: '))
  ages.append(age)
  
# Calculate ticket price
for age in ages:
  if (age < 18):  # 25$/1 child, age under 18
    price += 25
  elif (18 <= age <= 60):  # 100$/1 adult, age from 18 to 60
    price += 100
  else:  # 50$/ 1 old, age upper than 60
    price += 50

# total money for those people's tickets
print(f'The total money for tickets is ${price}')
#TODO use f-string
