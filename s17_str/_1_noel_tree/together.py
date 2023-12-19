total_height=6
for h in range(1, total_height + 1):
  print(h, end='')

  # haft tree ontheleft
  # print other half ontheleft at height=h, starnum=h-1, rjust=total_height   # ref Duy  # ref Phuong
  # print other half ontheleft at height=1, starnum=0,   rjust=6              #          #
  # print other half ontheleft at height=2, starnum=1,   rjust=6              # ref Duy
  # print other half ontheleft at height=2, starnum=2,   rjust=6              # ref Hieu
  # print other half ontheleft at height=4, starnum=3,   rjust=6              # ref Hieu
  # print other half ontheleft at height=5, starnum=4,   rjust=6              # ref Hieu
  # print other half ontheleft at height=6, starnum=5,   rjust=6              # ref Hieu
  print( ('*'*(h-1)).rjust(total_height), end='')

  # haft tree ontheright
  print('*'*h)

'''
1 *          .*              .     *
2 **         .***            .    ***
3 ***        .*****          .   *****
4 ****       .*******        .  *******
5 *****      .*********      . *********
6 ******     .***********    .***********
z *          .*              .     *
'''
