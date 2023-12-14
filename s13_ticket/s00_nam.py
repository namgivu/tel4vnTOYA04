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
def tien_ve(tuoi):
  if                60<tuoi : return 50
  if      18<=tuoi<=60      : return 100
  if tuoi<18                : return 25

n = input('nhap n: ')
n = int(n)

print()
tongtien=0
for i in range(1,n+1):
  t = input(f'nhap tuoi nguoi thu {i=}: ')
  t = int(t)

  g = tien_ve(t)
  tongtien += g

  print(f'{tien_ve(t)=} -> {tongtien=}')
  print()

print(f'{tongtien=}')
