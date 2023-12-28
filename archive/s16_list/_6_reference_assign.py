l = [1,2,3,4,5]
print(l)

l2 = l  # make two variables l and l2 pointing into the same list
        # tạo hai biến l và l2 cùng trỏ vào một danh sách giá trị
print(l2)

l .append(6)
l2.append(7)
print(f'{l=}')
print(f'{l2=}')

### use .copy() to have l2 as new list
l3 = l.copy()
l3.append(8)
print(f'{l=}')
print(f'{l3=}')
