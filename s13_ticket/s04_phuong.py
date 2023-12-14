n = int(input(f'nhap so luong nguoi mua ve: '))

i = 1
s = 0
while i <= n:
    age = int(input(f'nhap tuoi nguoi thu {i}: '))
    if age >= 18 and age <= 60:
        s = s + 100
    elif age < 18:
        s = s + 25
    elif age > 60:
        s = s + 50
    i = i + 1

print (f'Tong tien ve cho {n} nguoi la: {s}$')
