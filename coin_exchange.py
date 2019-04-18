money = int(input())
coins = [0] * 4
print('money to exchange: %d won' % money)

coins[0] = money // 500
money %= 500
coins[1] = money // 100
money %= 100
coins[2] = money // 50
money %= 50
coins[3] = money // 10
money %= 10

for (val, coin) in zip([500, 100, 50, 10], coins):
    print('coin of %d won: %d' % (val, coin))
print('change left: %d won' % money)
