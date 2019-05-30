def plus(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print(plus(1, 2, 3, 4))
