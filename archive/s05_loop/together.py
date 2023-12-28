# bangcuuchuong 5 @ Nam
for i in range(1,9+1):
  #print('5 * ' + str(i) )
  print(f'5 * {i} = {5*i}')

print()

# in ra tu 0 den 9 @ Huong
for i in range (0,10):
  print(i)

print()

# in cac so chan tu 10 den 20 @ Phuong
for i in range(10,21,2):
  print(i)

print()

# in cac so chia het cho 3 tu 30 den 60 @ Hieu kasumo  # i % 3 == 0
for i in range(30,60+1):
  if i % 3 == 0:
    print(i)

print()

# in cac so le, tu 60 den 90 @ Huynh kuzo
for i in range(61,90+1,2):
  print(i)

print()

# in cac so chan chia het cho 3 tu 90 den 100 @ Cuong
for i in range(90,100+1):
  if i % 3 == 0 and i % 2 == 0:
    print(i)

//
for i in range (1,10):
  n = radom.randint(1,10)
  print (n)