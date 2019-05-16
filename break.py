total = 0
for i in range(1, 11, 1):
    print("%2dth loop" % i)
    if (i == 3):
        break
    total += i;
print(total)