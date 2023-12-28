# .venv/bin/python -m pyflowchart main.py -o ./pyflowchart/flowchart.html
debugstart=''

def in_chaohoi():
  print('xin chao!')
  print('ban khoe khong?')

in_chaohoi()
in_chaohoi()


def chao(name):
  print('chao ' + name)

chao(name='tel4vn')
chao(name='toya04')


#region convert_to_mb(gb=2)
'''
convert_to_mb(gb=2) -> 1024*2 = 2048
convert_to_mb(gb=4) -> 1024*4 = 4096

---
SSD 1Tb
RAM 4Gb
baonhieu Mb?

1Tb = 1024Gb
         1Gb = 1024Mb 

tudien == bit == codien/kocodien == 1/0  -> binary hecoso2
1byte  ==8bit
2^10 = 1024

tan = 1000kg
         1kg = 1000g
'''
def convert_to_mb(gb):
  return gb * 1024

print( convert_to_mb(1) )
print( convert_to_mb(2) )
print( convert_to_mb(gb=3) )
mb=convert_to_mb(gb=4) ; print(mb)
#endregion convert_to_mb(gb=2)

debugend=''
