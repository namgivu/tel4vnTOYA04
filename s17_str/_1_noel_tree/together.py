
def printnoeltree(total_height=6):
  r = []

  digitlen = len(str(total_height))  # digitlen(total_height)
  for h in range(1, total_height + 1):
    s1 = str(h).rjust(digitlen)
    #        h bug here for height>=10
    #        h -> rjust(digitlen(total_height) )

    print(s1, end='')

    # haft tree ontheleft
    # print other half ontheleft at height=h, starnum=h-1, rjust=total_height   # ref Duy  # ref Phuong
    # print other half ontheleft at height=1, starnum=0,   rjust=6              #          #
    # print other half ontheleft at height=2, starnum=1,   rjust=6              # ref Duy
    # print other half ontheleft at height=2, starnum=2,   rjust=6              # ref Hieu
    # print other half ontheleft at height=4, starnum=3,   rjust=6              # ref Hieu
    # print other half ontheleft at height=5, starnum=4,   rjust=6              # ref Hieu
    # print other half ontheleft at height=6, starnum=5,   rjust=6              # ref Hieu
    s2 = ('*'*(h-1)).rjust(total_height)
    print(s2, end='')

    # haft tree ontheright
    s3 = '*'*h
    print(s3)
    r.extend([s1+s2+s3])

  s = '*'.rjust(total_height+2)
  print(s)
  r.extend([s])

  return r

  print()
  '''
  1 *          .*              .     *
  2 **         .***            .    ***
  3 ***        .*****          .   *****
  4 ****       .*******        .  *******
  5 *****      .*********      . *********
  6 ******     .***********    .***********
  z *          .*              .     *
  '''

printnoeltree(total_height=1)
printnoeltree(total_height=2)
printnoeltree(total_height=3)
printnoeltree(total_height=6)
printnoeltree(total_height=9)
printnoeltree(total_height=12)

r=printnoeltree(total_height=6)
r.reverse()
print()
print('\n'.join(r) )
