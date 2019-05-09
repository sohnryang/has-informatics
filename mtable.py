n = int(input())
assert 2 <= n <= 9
print('\n'.join(["%d * %d = %2d" % (n, i + 1, n * (i + 1)) for i in range(9)]))
