"""
similar labw1.2 but even num only from 1 to 20

Writing a program that let user guess a secret even number from 1 to 20
a. Using random package to generate a number.
b. User only has 5 tries to guess.
c. If it lower than the secret_number: print that user’s number is lower.
d. If it higher than the secret_number: print that user’s number is higher.
e. If user guess no more than 5 tries, they win the game.
"""

# ref Huong @ import package
import random

# ref Duy @ generate secret even number from 1 to 20 
secret_number = random.randrange(0, 20, step=2)

''' ref Huynh kuzo @ b. User only has 5 tries to guess ''' 
i =1
while i <= 5:
  # ref Duy @ user input their guess ; cast it to int()
  so = int(input('Enter an even num from 0 to 20: '))  #Nam NOTE: Duy to use single quote ' # cho nay chua tab
  
  # ref Hieu @ If it lower than the secret_number: print t hat user’s number is lower.
  if so < secret_number:  #Phuong NOTE: Hieu khong can dieu kien (secret_number % 2 == 0)
    print('So cua ban nho hon so bi mat')
    i = i + 1
  
  # ref Cuong @ d. If it higher than the secret_number: print that user’s number is higher.
  if so > secret_number:
    print('So cua ban lon hon so bi mat')
    i = i + 1
  
  if so == secret_number:
    print('Ban da doan dung!')
    break

if i > 5:
  print('Ban da thua cuoc')

print(f'So bi mat la {secret_number}')
