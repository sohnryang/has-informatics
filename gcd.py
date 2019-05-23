num1, num2 = map(int, input().split())
gcd = 1
for i in range(1, num1 + 1):
    if num2 % i == 0 and num1 % i == 0:
        gcd = i
print(gcd)

nums = [num1, num2]
nums.sort()
while nums[1] % nums[0] != 0:
    nums[1] %= nums[0]
    nums.sort()
print(nums[0])
