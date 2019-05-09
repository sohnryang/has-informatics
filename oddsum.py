n = int(input())

def shorter():
    print(sum(range(1, n + 1, 2)))

def longer():
    result = 0
    for i in range(1, n + 1, 2):
        result += i
    print(result)

longer()
