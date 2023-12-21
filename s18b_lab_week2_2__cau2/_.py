"""
Reading logs file

nginx log sample.log

Log format is:
<ip> - - <date-time> <request> <http code> <body size><host> <user-agent>
eg
<ip>          - - <date-time>                  <request>              <http code>
66.249.65.159 - - [05/Oct/2022:19:10:38 +0600] "GET /sample HTTP/1.1" 404 177 "https://example.com" "Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
172.25.65.3   - - [06/Oct/2022:19:11:24 +0600] "GET /sample HTTP/1.1" 200 4223 "https://example.com" "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
                                                                          <body size><host>          <user-agent>

Write  a python function  to  read  from this  log  file
and print  out  this in formation:
-Total of success (2xx) and failed (4xx, 5xx) requests
-Output the client ip that has the most 4xx request
"""

from pathlib import Path

#region get SH
print(__file__)
THIS_FILE     = __file__

THIS_FILE_DIR = Path(__file__).parent
SH            = THIS_FILE_DIR

SH = THIS_FILE_DIR = Path(__file__).parent  # SH aka SCRIPT_HOME
print(SH)
#endregion get SH

logfile_p = SH/'sample.log'
fc        = logfile_p.read_text()
logline_list = fc.split('\n')

#region split
def sol_split():
  r = []
  for line in logline_list[:-4]:
    print(line)
    ip = line.split(' - - ')[0]

    afterip = line.split(' - - ')[1]
    errcode = afterip.split('"')[2].split(' ')[1]

    print(f'{ip=:>} {errcode=:>}')
    print()
    r.append(
      [ip,errcode]
    )
  print(r)

  '''
  TODO Duy 
  [
    ['66.249.65.159', '404'], 
    ['172.25.65.3',   '200'], 
    ['185.19.60.62',  '200'], 
    ['47.29.201.179', '500'], ['66.249.65.159', '401'], ['47.29.201.179', '200'], ['47.29.201.179', '205'], ['66.249.65.159', '403'], ['47.29.201.179', '502'], ['66.249.65.159', '403'], ['47.29.201.179', '201']]
  dem so luong 4xx
  dem so luong 5xx
  '''
  def cach0_volong():
    dem=0
    for e in r:
      if e[1].startswith('4') or e[1].startswith('5') :
        print(e[1])
        dem+=1
    print(f'{dem=}')

  print(
    '4xx 5xx count: ',
    len(
      [ e for e in r  if e[1].startswith('4') or e[1].startswith('5') ]
      # e for e ....  if filter1              or filter2
    )
  )

sol_split()
#endregion split

#TODO regex

debug=122