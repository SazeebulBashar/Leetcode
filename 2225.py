import collections
def findWinners(matches):
    ans = [[] for _ in range(2)]
    lossesCount = collections.Counter()

    for winner, loser in matches:
      if winner not in lossesCount:
        lossesCount[winner] = 0
      lossesCount[loser] += 1

    print(lossesCount)
    
    for player, nLosses in lossesCount.items():
      if nLosses < 2:
        ans[nLosses].append(player)

    return [sorted(ans[0]), sorted(ans[1])]

print(findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))