import re  # regex regular expression  # ref https://regex101.com/
print('1'=='1')
print('1'=='122')

nowtime = '2023-12-12 08:38:00 PM'
#       =  date       time     ampm
nowtime = '2023-11-22 01:23:45 AM'

#region not using regex
print(     nowtime.split(' ') )
D,t,ampm = nowtime.split(' ')

# y,m,d <= D
y,m,d = D.split('-')
H,M,S = t.split(':')
#endregion not using regex

print()

### w/ regex
m  = re.findall(r'(.*) (.*) (.*)',                 nowtime)
m2 = re.findall(r'(\d*-\d*-\d*) (.*) (.*)',        nowtime)
m3 = re.findall(r'((\d*)-(\d*)-(\d*))  (.*) (.*)', nowtime)

m = re.findall(r'(.*) (.*) (.*)', nowtime)
D,t,ampm = m[0]

mD = re.findall(r'(\d\d\d\d)-(\d\d)-(\d\d)', D)
y  = mD[0][0]
m  = mD[0][1]
d  = mD[0][2]

m  = re.findall(r'(\d\d\d\d)-(\d\d)-(\d\d).*', nowtime)
y2 = mD[0][0]
M2 = mD[0][1]
d2 = mD[0][2]

m  = re.findall(r'.* ((\d\d):(\d\d):(\d\d)) .*(AM|PM)', nowtime)


### check valid email
email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$"
#  =                       , email
m  = re.findall(email_regex, 'no-reply@google.com')
if m: print('Valid')

m2 = re.findall(email_regex, 'email.google')
if m2: print('Valid')
else:  print('Invalid')
