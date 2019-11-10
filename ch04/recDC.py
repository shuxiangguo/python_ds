# 找零钱算法


import time


# 递归版本
def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins

    return minCoins


start = time.time()
print(recMC([1,5,10,25], 63))
end = time.time()
length = end - start
print(length)


# 添加查询表后的版本
def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c < change]:
            numCoins = 1 + recDC(coinValueList, change-i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


start = time.time()
print(recDC([1,5,10,25], 63, [0]*64))
end = time.time()
length = end - start
print(length)


# 动态规划版本找零问题
def dpMakeChange(coinValueList, change, minCoins, coinUsed):
    for cents in range(change+1):
        coinCount = cents
        new_coin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                new_coin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = new_coin
    return minCoins[change]


def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


c1 = [1,5,10,21,25]
coinUsed = [0]*64
coinCount = [0]*64

cnt = dpMakeChange(c1, 63, coinCount, coinUsed)
print(cnt)

printCoins(coinUsed, 63)
printCoins(coinUsed, 52)
print(coinUsed)
