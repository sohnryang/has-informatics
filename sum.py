def constant_time():
    n = int(input())
    print((n + 1) * n // 2)

def loop():
    n = int(input())
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

loop()
