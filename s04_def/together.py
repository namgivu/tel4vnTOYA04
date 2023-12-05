def mu2(i):  # by Phuong
  return 2**i

r=mu2(0) ; print(r)  # 1 2^0
r=mu2(1) ; print(r)  # 2 2^1
r=mu2(2) ; print(r)  # 4 2^2
r=mu2('3') ; print(r)  # 4 2^2

import sys; sys.exit()

###

def tong2so(a,b):  # by Hieu kasumo
  return a+b
r=tong2so(1,   22)   ; print(r)  # 23
r=tong2so(333, 4444) ; print(r)  # 4777

###

def tong3so (a,b,c):  # by Huong
  return a+b+c
r=tong3so(1,22,333) ; print(r)  # 356
r=tong3so(4444,
          55555,
          666666) ; print(r)  # 726665

###

def max2so(num1, num2):  # by Duy
  max = num1
  if num1 <= num2:
    max = num2
  return max
  
r=max2so(1,22)      ; print(r)  # 22
r=max2so(4444, 333) ; print(r)  # 4444

###

def min2so(a, b): # by Huynh kuzo 
  min = a
  if a >= b:
    min = b
  return min
r=min2so(1,22)      ; print(r)  # 1
r=min2so(4444, 333) ; print(r)  # 333
r=min2so(-1, -2)    ; print(r)  # -2

###
print()
print()

def min3so_1(a, b, c): # by Mai Cuong
  if a <= b and a <=c: return a
  if b <= a and b <=c: return b
  if c <= a and c <=b: return c
r=min3so_1(1, 22,  333) ; print(r)  # 1
r=min3so_1(1,-22,  333) ; print(r)  # -22
r=min3so_1(1, 22, -333) ; print(r)  # -333


def min3so_2(a, b, c): # by Mai Cuong
  min = a
  if b < min:
    min = b
    
  if c < min:
    min = c
  return min

r1=min3so_2(1, 22,  333) ; print(r1)  # 1
r1=min3so_2(1,-22,  333) ; print(r1)  # -22
r1=min3so_2(1, 22, -333) ; print(r1)  # -333


def min3so_3(a, b, c): # by Nam
  min = a if a<b   else b
  min = c if c<min else min
  return min

r1=min3so_3(1, 22,  333) ; print(r1)  # 1
r1=min3so_3(1,-22,  333) ; print(r1)  # -22
r1=min3so_3(1, 22, -333) ; print(r1)  # -333
