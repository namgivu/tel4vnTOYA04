"""
Writing a program that let user guess a secret number from 1 to 10
a. Using random package to generate a number.
b. User only has 5 tries to guess.
c. If it lower than the secret_number: print that user’s number is lower.
d. If it higher than the secret_number: print that user’s number is higher.
e. If user guess no more than 5 tries, they win the game.

n=1
1 2 3 4 5 6 7 8 9 10
     lt 5 gtwhi
"""

# ref Huong @  a. Using random package to generate a number  # only write import
import random

# ref Phuong @ generate aa secret number from 1 to 10
secret_number = random.randint(1, 10)
print (secret_number)

### start @ let user guess 

'''
ref Phuong @  b. User only has 5 tries to guess.
'''
i = 1
while i<=5:
  # ref Cuong @ nhap so nguoichoi doan  > Moi ban doan so? 
  so = input('Moi ban doan so? ')
  so = int(so)
  
  # ref Cuong @  c. If it lower than the secret_number: print that user’s number is lower.
  if so < secret_number:
    print('So cua ban nho hon sobimat')
    i = i + 1
  
  # ref Hieu kasumo @  d. If it higher than the secret_number: print that user’s number is higher.
  if int(so) > int(secret_number): 
    print('So cua ban lon hon so bi mat')
    i = i + 1
    
  if so == secret_number:
    print ('Chuc mung ban da doan dung!')
    break

if i > 5:
  print ('Ban da thua cuoc')

print(f'{secret_number=:>}')
