import json

hocvien = {
  'ten'     : 'Nam G VU',
  'namsinh' : 1982,
  'cungu'   : 'Quan 10, Saigon',

  'lop da hoc': [],
}
print(hocvien)

hocvien['lop da hoc'].append('toya04')
print(hocvien)

hocvien['keybanmuonthem'] = 'giatri'
print(hocvien)
print(json.dumps(hocvien, indent=2))

print('\n### ###\n')

hocvien2 = {
  'ten'       : 'Hieu',
  'lop da hoc': ['toya04'],
}

hocvien_danhsach = [hocvien, hocvien2]
print(json.dumps(hocvien_danhsach, indent=2))
