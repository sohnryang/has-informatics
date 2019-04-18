money = int(input())
coin_values = [500, 100, 50, 10]

print('money to exchange: %d won' % money)
for val in coin_values:
    print('coin of %d won: %d' % (val, money // val))
    money %= val
print('change left: %d won' % money)
